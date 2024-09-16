// date => yyyy-mm-dd hh:mm:ss
const formatTime = date => {
  const year = date.getFullYear()
  const month = date.getMonth() + 1
  const day = date.getDate()
  const hour = date.getHours()
  const minute = date.getMinutes()
  const second = date.getSeconds()

  return `${[year, month, day].map(formatNumber).join('-')} ${[hour, minute, second].map(formatNumber).join(':')}`
}
// date => yyyy-mm-dd
const formatDate = (date, formatType) => {
  const year = date.getFullYear()
  const month = date.getMonth() + 1
  const day = date.getDate()
  if (formatType === 'Ch') {
    return `${year}年${month}月${day}日`
  } else {
    return [year, month, day].map(formatNumber).join('-')
  }
}
const formatNumber = n => {
  n = n.toString()
  return n[1] ? n : `0${n}`
}

// 获取url上的参数
function getQueryString(name) {
  var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)", "i");
  var r = window.location.href.match(reg);
	console.log(window.location.href)
	console.log(r)
  if (r != null) return unescape(r[2]); return null;
}

module.exports = {
  formatTime,
  formatDate,
	getQueryString
}
