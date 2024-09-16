import service from '@/utils/request'

export function newsCateList(data) {
  return service({
    url: '/newsCateList',
    method: 'post',
    data
  })
}

export function newsList(data) {
  return service({
    url: '/newsList',
    method: 'post',
    data
  })
}

export function newsDetail(data) {
  return service({
    url: '/newsDetail',
    method: 'post',
    data
  })
}

export function newsFav(data) {
  return service({
    url: '/newsFav',
    method: 'post',
    data
  })
}

export function newsFavList(data) {
  return service({
    url: '/newsFavList',
    method: 'post',
    data
  })
}