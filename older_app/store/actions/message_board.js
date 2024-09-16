import { messageBoardSend } from '@/api/message_board.js'

export default {
  async messageBoardSend({ }, data) {
    return messageBoardSend(data)
  }
}

