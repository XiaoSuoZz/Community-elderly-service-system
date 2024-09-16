import { login, register, userDetail, userEdit, areaList, instantCallAdd } from '@/api/user'

export default {
  async login({ commit }, data) {
		const ret = await login(data)
		if(ret.code == 0) {
			commit('SET_USER_INFO', ret.data)
		}
    return ret
  },
  async register({ commit }, data) {
    return register(data)
  },
	async userDetail({ commit }, data) {
    return userDetail(data)
  },
	async userEdit({ commit }, data) {
    return userEdit(data)
  },
  async areaList({ commit }, data) {
		const ret = await areaList(data)
		if(ret.code == 0) {
			commit('SET_AREA_LIST', ret.data)
		}
    return ret
  },
	async instantCallAdd({ commit }, data) {
    return instantCallAdd(data)
  }
}

