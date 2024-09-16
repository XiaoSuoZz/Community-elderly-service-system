<template>
	<view class="video">
		<u-sticky bgColor="#fff">
			<u-tabs :list="favTypeList" @change="onChangeTab"></u-tabs>
		</u-sticky>
		<view class="list-wrpper">
			<view v-if="!loading">
				<view v-if="list.length === 0" class="empty-wrapper">
					<u-empty mode="news" iconSize="180" marginTop="200" text="暂无收藏"></u-empty>
				</view>
				<view class="video-list">
					<view v-for="(item,index) in list" class="video-item" @click="onSelect(item)">
						<view v-if="tabIndex == 1" class="video-image-wrapper">
							<img :src="item.video_info.img_url"></img>
						</view>
						<view :class="{ newsInfoWrapper: tabIndex == 0 }" class="video-info-wrapper">
							<view class="video-title">{{ item.info.title }}</view>
							<view class="video-time">{{ item.info.create_time}}</view>
						</view>
					</view>
				</view>
			</view>
		</view>
	</view>
</template>

<script>
	import { mapGetters, mapActions } from 'vuex'
	import { getQueryString, formatDate } from '../../../utils/utils.js'
	export default {
		data() {
			return {
				favTypeList: [
					{ id: 1, name: '新闻资讯' },
					{ id: 2, name: '视频课堂' },
				],
				tabIndex: 0,
				// 视频列表
				list: [],
				loading: false
			};
		},
		computed: {
			...mapGetters([
				'getUserInfo'
			])
		},
		async mounted() {
			if (!this.getUserInfo) {
				uni.redirectTo({
					url: `../../login/login`
				})
			}
			this.getNewsList()
		},
		methods: {
			...mapActions({
				actionVideoFavList: 'videoFavList',
				actionNewsFavList: 'newsFavList'
			}),
			// 切换tab
			onChangeTab(e) {
				const { index } = e
				this.tabIndex = index
				if (index == 0 ) {
					this.getNewsList()
				} else {
					this.getVideoList()
				}
			},
			// 进入详情页
			onSelect(item) {
				if (this.tabIndex == 0) {
					const { id, title } = item.news_info
					uni.navigateTo({
						url: `../../news/detail/detail?title=${title}&id=${id}`
					})					
				} else {
					const { id, title } = item.video_info
					uni.navigateTo({
						url: `../../video/detail/detail?title=${title}&id=${id}`
					})
				}
			},
			// 获取收藏列表
			async getNewsList() {
				this.loading = true
				uni.showLoading({
					mask: true
				})
				const ret = await this.actionNewsFavList(Object.assign({user_id: this.getUserInfo.id}))
				uni.hideLoading()
				this.loading = false
				if(ret.code == 0) {
					const list = ret.data
					for (let item of list) {
						item.create_time = formatDate(new Date(item.create_time))
						item.news_info.create_time = formatDate(new Date(item.news_info.create_time))
						item.info = item.news_info
					}
					this.list = list
				}
			},
			// 获取收藏列表
			async getVideoList() {
				this.loading = true
				uni.showLoading({
					mask: true
				})
				const ret = await this.actionVideoFavList(Object.assign({user_id: this.getUserInfo.id}))
				uni.hideLoading()
				this.loading = false
				if(ret.code == 0) {
					const list = ret.data
					for (let item of list) {
						item.video_info.img_url = `../../../api/${item.video_info.img_url}`
						item.create_time = formatDate(new Date(item.create_time))
						item.video_info.create_time = formatDate(new Date(item.video_info.create_time))
						item.info = item.video_info
					}
					this.list = list
				}
			},
		}
	}
</script>

<style lang="scss">
.video-list {
	width: 100%;
	padding: 30rpx 20rpx;
	box-sizing: border-box;
	.video-item {
		width: 100%;
		padding: 20rpx;
		border-bottom: solid 1px #F1F1F1;
		display: flex;
		box-sizing: border-box;
		.video-image-wrapper {
			width: 300rpx;
			height: 200rpx;
			flex: 0;
			img {
				width: 300rpx;
				height: 200rpx;
			}
		}
		.video-info-wrapper {
			flex: 1;
			box-sizing: border-box;
			height: 200rpx;
			display: flex;
			flex-direction: column;
			justify-content: space-between;
			align-items: flex-start;
			padding-left: 20rpx;
			.video-title {
				font-size: 34rpx;
				color: #333;
				font-weight: bold;
				text-indent: 30rpx;
			}
			.video-time {
				color: #999;
				width: 100%;
				text-align: end;
			}
		}
		.newsInfoWrapper {
			height: auto;
		}
	}
}
</style>
