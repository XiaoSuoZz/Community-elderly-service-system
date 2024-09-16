<template>
	<view class="container">
		<view class="banner-wrap">
			<image :src="banners[currentBannerIndex]" mode="aspectFill"></image>
		</view>
		<!-- 列表 -->
		<view class="video-list">
			<view v-for="(item,index) in videoList" class="video-item" @click="onSelectVideo(item)">
				<view class="video-image-wrapper">
					<img :src="item.img_url"></img>
				</view>
				<view class="video-info-wrapper">
					<view class="video-title">{{ item.title }}</view>
					<view class="video-time">{{ item.create_time}}</view>
				</view>
			</view>
		</view>
		<!-- 更多按钮 -->
		<view class="more-serve-wrapper">
			<!-- 上门预约 -->
			<view class="serve-item appointment" @click="onGoAppointment">
				<image src="../../static/icon/appointment.png" class="serve-icon"></image>
				<view class="serve-title">上门预约</view>
			</view>
			<!-- 预约记录 -->
			<view class="serve-item record" @click="onGoRecord">
				<image src="../../static/icon/record.png" class="serve-icon"></image>
				<view class="serve-title">服务记录</view>
			</view>
			<!-- 一件呼救 -->
			<view class="serve-item sos" @click="onInstantCall">
				<image src="../../static/icon/sos.png" class="serve-icon"></image>
				<view class="serve-title">一键呼救</view>
			</view>
		</view>
	</view>
</template>

<script>
	import { mapGetters, mapActions } from 'vuex'
	import { formatDate } from '../../utils/utils.js'
	export default {
		data() {//在 data 中定义了 banners 和 currentBannerIndex 来存储轮播图的图片列表和当前显示的图片索引
			return {
				lastCallTime: null,
				banners: [
					'../../static/banner/1.jpg',
					'../../static/banner/2.jpg'
				],
				currentBannerIndex: 0,
				timer: null,
				videoList: []
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
					url: `../login/login`
				})
			}//在 mounted 生命周期钩子中启动定时器，定时切换 currentBannerIndex
			this.clearTimer()
			this.timer = setInterval(() => {
				let index = this.currentBannerIndex + 1
				if (index > this.banners.length - 1) {
					index = 0
				}
				this.currentBannerIndex = index
			}, 3000)
			this.getVideoList()
		},
		beforeMount() {
			this.clearTimer()
		},
		methods: {//在 beforeMount 生命周期钩子中以及其他需要的地方调用 clearTimer 方法清除定时器，避免内存泄漏。
			...mapActions({
				actionInstantCallAdd: 'instantCallAdd',
				actionVideoList: 'videoList'
			}),
			clearTimer() {
				if(this.timer) {
					clearInterval(this.timer)
					this.timer = null
				}
			},
			// 一键呼叫  5分钟间隔
			async onInstantCall() {
				const now = new Date().getTime()
				if (this.lastCallTime && now - this.lastCallTime < 5 * 60 * 1000) {
					uni.showToast({
						icon: 'none',
						title: '请勿频繁操作'
					})
					return
				}
				uni.showLoading({
					mask: true
				})
				const ret = await this.actionInstantCallAdd({user_id: this.getUserInfo.id})
				uni.hideLoading()
				if(ret.code == 0) {
					uni.showToast({
						icon: 'none',
						title: '呼叫成功'
					})
					this.lastCallTime = now
				}
			},
			// 获取视频列表
			async getVideoList() {
				const ret = await this.actionVideoList({
					page_index: 1,
					page_size: 10
				})
				if(ret.code == 0) {
					const { list, total_count } = ret.data
					for (let item of list) {
						item.img_url = `api/${item.img_url}`
						item.create_time = formatDate(new Date(item.create_time))
					}
					this.videoList = list
				} 
			},
			onGoAppointment() {
				uni.navigateTo({
					url: "./appointment/appointment"
				})
			},
			onGoRecord() {
				uni.navigateTo({
					url: "../my/record/record"
				})
			}
		}
	}
</script>

<style lang="scss">
	page {
	  background-color:#f8f8f8;
	}
	.container {
		// padding-top: 40vh;
		height: calc(100vh - 94px);
		overflow: hidden;
		display: flex;
		flex-direction: column;
		box-sizing: border-box;
		.banner-wrap {
			width: 100%;
			height: 200px;
			flex-shrink: 0;
			image {
				width: 100%;
				height: 100%;
				object-fit: contain;
			}
		}
		.video-list {
			flex: 1;
			padding-bottom: 145px;
			overflow-y: scroll;
		}
	}
	.video-list {
		width: 100%;
		padding: 12rpx 0rpx;
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
					object-fit: cover;
					background-color: #ddd;
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
		}
	}
	.more-serve-wrapper {
		position: absolute;
		background-color: #f8f8f8;
		left: 0;
		bottom: 0;
		width: 100%;
		padding: 12px 20rpx;
		display: flex;
		align-items: center;
		justify-content: space-between;
		gap: 12px;
		box-sizing: border-box;
		.serve-item {
			width: 200rpx;
			height: 180rpx;
			border-radius: 20rpx;
			display: flex;
			flex-direction: column;
			align-items: center;
			justify-content: space-between;
			padding: 20rpx;
			box-shadow: 10rpx 10rpx 20rpx rgba($color: #000000, $alpha: .2);
			.serve-icon {
				width: 140rpx;
				height: 140rpx;
			}
			.serve-title {
				width: 100%;
				text-align: center;
				font-weight: bold;
				font-size: 40rpx;
				color: #fff;
			}
		}
		.appointment {
			background-color: #3c9cff;
			&:hover {
				background-color: #2b85e4;
			}
		}
		.record {
			background-color: #ff9900;
			&:hover {
				background-color: #f29100;
			}
		}
		.sos {
			background-color: #DC143C;
			&:hover {
				background-color: #FF1493;
			}
		}
	}
</style>
