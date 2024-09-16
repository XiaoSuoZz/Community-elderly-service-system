let BaseUrl="http://127.0.0.1:8000/"
// 数据请求
function ToDJ(relativeUrl) {
	return BaseUrl + relativeUrl
}
// 提示
// 成功提示
function NotifySuc(self, str) {
	self.$notify.success({
		title: str,
		showClose: false
	});
}
// 错误提示
function NotifyFail(self, str) {
	self.$notify.error({
		title: str,
		showClose: false
	});
}

// 操作确认
function Confirm(self, title, message) {
	return new Promise(resolve => {
		self.$confirm(message || '确认操作', title || '提示', {
			confirmButtonText: '确定',
			cancelButtonText: '取消',
			type: 'warning'
		}).then(() => {
			resolve(true)
		}).catch(() => {
			resolve(false)
		});
	})
}

function serverPost(url, data) {
	return new Promise(resolve => {
		axios.post(url, new URLSearchParams(data)).then(res => {
			resolve(res.data)
    })
	})
}

// 获取url上的参数
function getQueryString(name) {
  var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)", "i");
  var r = window.location.search.substr(1).match(reg);
  if (r != null) return unescape(r[2]); return null;
}

const FormatDate = date => {
  const year = date.getFullYear()
  const month = date.getMonth() + 1
  const day = date.getDate()
  return `${[year, month, day].map(formatNumber).join('-')}`
}

const FormatTime = date => {
  const hours = date.getHours()
  const minute = date.getMinutes()
  const second = date.getSeconds()
  return `${[hours, minute, second].map(formatNumber).join(':')}`
}

const formatNumber = n => {
  n = n.toString()
  return n[1] ? n : `0${n}`
}