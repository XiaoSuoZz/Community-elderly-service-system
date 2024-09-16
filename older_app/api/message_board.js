import service from '@/utils/request'

export function messageBoardSend(data) {
  return service({
    url: '/messageBoardSend',
    method: 'post',
    data
  })
}
