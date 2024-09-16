import Vue from 'vue'
import Vuex from 'vuex'
import getters from './getters'
import actions from './actions'

Vue.use(Vuex)

const state = {
	// 用户信息
  userInfo: null,
	// 视频分类
	videoCateList: [],
	// 新闻分类
	newsCateList: [],
	// 地区
	areaList: []
}

const mutations = {
  SET_USER_INFO: (state, data) => {
    state.userInfo = data
  },
  SET_VIDEO_CATE: (state, data) => {
    state.videoCateList = data
  },
	SET_NEWS_CATE: (state, data) => {
    state.newsCateList = data
  },
	SET_AREA_LIST: (state, data) => {
    state.areaList = data
  }
}

const store = new Vuex.Store({
  state,
  mutations,
  actions,
  getters
})

export default store
