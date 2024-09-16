import service from '@/utils/request'

export function videoCateList(data) {
  return service({
    url: '/videoCateList',
    method: 'post',
    data
  })
}

export function videoList(data) {
  return service({
    url: '/videoList',
    method: 'post',
    data
  })
}

export function videoDetail(data) {
  return service({
    url: '/videoDetail',
    method: 'post',
    data
  })
}

export function videoFav(data) {
  return service({
    url: '/videoFav',
    method: 'post',
    data
  })
}

export function videoFavList(data) {
  return service({
    url: '/videoFavList',
    method: 'post',
    data
  })
}