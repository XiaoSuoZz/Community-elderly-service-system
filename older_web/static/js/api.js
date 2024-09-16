import service from './request.js'
const BaseUrl = 'http://127.0.0.1:8000/'
// export default {
//   // BaseUrl: 'http://127.0.0.1:8000/',
//   // 工作人员
//   // 登录
//   staffLogin: (data) => {
//     return service.post(`${BaseUrl}/staffLogin`, data)
//   }
// }
export function staffLogin(data) {
  return service.post(`${BaseUrl}/staffLogin`, data)
}