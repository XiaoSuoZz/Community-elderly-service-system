<template>
	<view class="container">
		<view v-if="videoInfo">
			<view class="video">
				<!-- <video :show-mute-btn="show_mute_btn" :enable-play-gesture="enable_play_gesture" :show-center-play-btn="show_center_play_btn" :page-gesture="page_gesture" src="https://img.cdn.aliyun.dcloud.net.cn/guide/uniapp/%E7%AC%AC1%E8%AE%B2%EF%BC%88uni-app%E4%BA%A7%E5%93%81%E4%BB%8B%E7%BB%8D%EF%BC%89-%20DCloud%E5%AE%98%E6%96%B9%E8%A7%86%E9%A2%91%E6%95%99%E7%A8%8B@20181126-lite.m4v" controls></video> -->
				<video 
					:show-mute-btn="show_mute_btn" 
					:enable-play-gesture="enable_play_gesture" 
					:show-center-play-btn="show_center_play_btn" 
					:page-gesture="page_gesture" 
					:src="videoInfo.video_url" 
					controls></video>
			</view>
			<view class="content">
				<view class="header">
					<view class="title">{{videoInfo.title}}</view>
					<view class="info">
						<view>{{videoInfo.create_time}}</view>
						<view>
							<u-icon size="30" :name="videoInfo.fav==0? 'star':'star-fill'" color="#f0ad4e" @click="onFav"></u-icon>
						</view>
					</view>
				</view>
				<text class="text-content">{{videoInfo.content}}</text>
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
				page_gesture: true,
				show_center_play_btn: false,
				enable_play_gesture: true,
				show_mute_btn: true,
				id: '',
				videoInfo: null
			};
		},
		computed: {
			...mapGetters([
				'getUserInfo'
			])
		},
		async mounted() {
			const id = getQueryString('id')
			this.id = id
			if (!this.getUserInfo) {
				uni.redirectTo({
					url: `../../login/login`
				})
			}
			this.getDetail()
		},
		methods: {
			...mapActions({
				actionVideoDetail: 'videoDetail',
				actionVideoFav: 'videoFav'
			}),
			async getDetail() {
				const ret = await this.actionVideoDetail({ id: this.id, user_id: this.getUserInfo.id })
				if (ret.code == 0) {
					let data = ret.data
					data.video_url  = `../../../api/${data.video_url}`
					data.create_time = formatDate(new Date(data.create_time))
					this.videoInfo = ret.data
				}
			},
			// 收藏、取消收藏操作
			async onFav() {
				const ret = await this.actionVideoFav({ video_id: this.id, user_id: this.getUserInfo.id })
				if (ret.code == 0) {
					this.videoInfo.fav = this.videoInfo.fav == 1 ? 0 : 1
				}
			}
		}
	}
</script>

<style lang="scss">
	.container{
		width: 100vw;
		height: 100vh;
	}
	.video{
		width: 100vw;
		height: 30vh;
	}
	video{
		width: 100vw;
		height: 30vh;
	}
	.content {
		width: 100%;
		padding: 0 20rpx;
		box-sizing: border-box;
		.header {
			padding: 20rpx 0rpx;
			margin-bottom: 20rpx;
			background-color: white;
			border-bottom: 1rpx solid #f1f1f1;
			.title {
				color: #333;
				font-weight: bold;
			}
			.info {
				margin-top: 20rpx;
				width: 100%;
				display: flex;
				justify-content: space-between;
				align-items: center;
				color: #666;
			}
		}
		.text-content {
			color: #444;
		}
	}
</style>
