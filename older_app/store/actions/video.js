import { videoList, videoCateList, videoDetail, videoFav, videoFavorite, videoFavList } from '@/api/video'

export default {
  videoList({ }, data) {
    return videoList(data)
  },
  async videoCateList({ commit }, data) {
		const ret = await videoCateList(data)
		if(ret.code == 0) {
			commit('SET_VIDEO_CATE', ret.data.list)
		}
    return ret
  },
  videoFavorite({ }, data) {
    return videoFavorite(data)
  },
  videoFavList({ }, data) {
    return videoFavList(data)
  },
	videoDetail({ }, data) {
    return videoDetail(data)
  },
	videoFav({ }, data) {
    return videoFav(data)
  }
}
