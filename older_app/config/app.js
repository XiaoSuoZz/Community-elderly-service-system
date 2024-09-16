module.exports = {
	// 请求域名 格式： https://您的域名
	// #ifdef MP
	HTTP_REQUEST_URL: 'http://192.168.23.48:8000/',
	VUE_APP_WS_URL: `http://192.168.23.48:8000/`,
	// #endif

	// #ifdef H5
	//H5接口是浏览器地址
	HTTP_REQUEST_URL: 'http://127.0.0.1:8000/',
	VUE_APP_WS_URL: 'http://127.0.0.1:8000/',
	// #endif

	HEADER: {
		// 'content-type': 'application/json',
		'content-type': 'application/x-www-form-urlencoded',
		//#ifdef H5
		'Form-type': navigator.userAgent.toLowerCase().indexOf("micromessenger") !== -1 ? 'wechat' : 'h5',
		//#endif
		//#ifdef MP
		'Form-type': 'routine',
		//#endif
		//#ifdef APP-VUE
		'Form-type': 'app',
		//#endif
	}
};
