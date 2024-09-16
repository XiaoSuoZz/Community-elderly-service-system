import { newsList, newsCateList, newsDetail, newsFav, newsFavorite, newsFavList } from '@/api/news'

export default {
  newsList({ }, data) {
    return newsList(data)
  },
  async newsCateList({ commit }, data) {
		const ret = await newsCateList(data)
		if(ret.code == 0) {
			commit('SET_NEWS_CATE', ret.data.list)
		}
    return ret
  },
  newsFavorite({ }, data) {
    return newsFavorite(data)
  },
  newsFavList({ }, data) {
    return newsFavList(data)
  },
	newsDetail({ }, data) {
    return newsDetail(data)
  },
	newsFav({ }, data) {
    return newsFav(data)
  }
}
