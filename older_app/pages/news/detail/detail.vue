<template>
	<view class="container">
		<view v-if="newsInfo">
			<view class="content">
				<view class="header">
					<view class="title">{{newsInfo.title}}</view>
					<view class="info">
						<view>{{newsInfo.create_time}}</view>
						<view>
							<u-icon size="30" :name="newsInfo.fav==0? 'star':'star-fill'" color="#f0ad4e" @click="onFav"></u-icon>
						</view>
					</view>
				</view>
				<text class="text-content">{{newsInfo.content}}</text>
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
				newsInfo: null
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
				actionNewsDetail: 'newsDetail',
				actionNewsFav: 'newsFav'
			}),
			async getDetail() {
				const ret = await this.actionNewsDetail({ id: this.id, user_id: this.getUserInfo.id })
				if (ret.code == 0) {
					let data = ret.data
					data.create_time = formatDate(new Date(data.create_time))
					this.newsInfo = ret.data
				}
			},
			// 收藏、取消收藏操作
			async onFav() {
				const ret = await this.actionNewsFav({ news_id: this.id, user_id: this.getUserInfo.id })
				if (ret.code == 0) {
					this.newsInfo.fav = this.newsInfo.fav == 1 ? 0 : 1
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
