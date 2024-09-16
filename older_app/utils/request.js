import { HTTP_REQUEST_URL, HEADER } from '@/config/app';
import store from '../store';

const baseUrl = process.env.NODE_ENV === 'development' ? "/api" : "";
/**
 * 发送请求
 */
function baseRequest({url, method, data})
{
  let Url = HTTP_REQUEST_URL, header = HEADER;
	console.log('Url:', url, method, data)
  return new Promise((resolve, reject) => {
    uni.request({
      url: baseUrl + url,
      method: method || 'GET',
      header: header,
      data: data || {},
      success: (res) => {
        if (res.data.code != 0)
				uni.showToast({
					icon: 'none',
					title: res.data.data
				})
      },
      fail: (msg) => {
				console.error('网络请求出错', msg)
        reject('请求失败');
      },
			complete: (res) => {
				resolve(res.data, res)
			}
    })
  });
}

const request = {};

['options', 'get', 'post', 'put', 'head', 'delete', 'trace', 'connect'].forEach((method) => {
  request[method] = (api, data, opt) => baseRequest(api, method, data, opt || {})
});



export default baseRequest;