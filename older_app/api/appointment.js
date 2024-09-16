import service from '@/utils/request'

export function appointmentAdd(data) {
  return service({
    url: '/appointmentAdd',
    method: 'post',
    data
  })
}

export function appointmentList(data) {
  return service({
    url: '/appointmentList',
    method: 'post',
    data
  })
}

export function appointmentDateList(data) {
  return service({
    url: '/appointmentDateList',
    method: 'post',
    data
  })
}
