import { appointmentList, appointmentAdd, appointmentDateList } from '@/api/appointment'

export default {
  appointmentList({ }, data) {
    return appointmentList(data)
  },
	appointmentAdd({ }, data) {
    return appointmentAdd(data)
  },
	appointmentDateList({ }, data) {
    return appointmentDateList(data)
  }
}
