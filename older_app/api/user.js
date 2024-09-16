import service from '@/utils/request'

export function login(data) {
  return service({
    url: '/userLogin',
    method: 'post',
    data
  })
}

export function register(data) {
	console.log('export function register:', data)
  return service({
    url: '/userRegister',
    method: 'post',
    data
  })
}

export function userDetail(data) {
  return service({
    url: '/userDetail',
    method: 'post',
    data
  })
}

export function userEdit(data) {
  return service({
    url: '/userEdit',
    method: 'post',
    data
  })
}

export function areaList(data) {
  return service({
    url: '/areaList',
    method: 'post',
    data
  })
}

export function instantCallAdd(data) {
  return service({
    url: '/instantCallAdd',
    method: 'post',
    data
  })
}