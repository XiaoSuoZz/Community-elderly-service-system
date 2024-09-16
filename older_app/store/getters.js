const getters = {
  getUserInfo: state => {
    return state.userInfo
  },
  getVideoCateList: state => {
    return state.videoCateList
  },
  getNewsCateList: state => {
    return state.newsCateList
  }
}

export default getters
