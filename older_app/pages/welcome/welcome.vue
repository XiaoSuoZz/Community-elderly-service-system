<template>
	<view class="container">
		<image class="logo" src="/static/logo.png"></image>
		<view class="slogon">
			<text class="title">社区老年人服务系统</text>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				
			}
		},
		onLoad() {
			console.log('welcome onload')
			setTimeout(() => {
				uni.redirectTo({
					url: '../login/login'
				})
			}, 2000)
		},
		methods: {
			
		}
	}
</script>

<style lang="scss">
	.container {
		display: flex;
		height: calc(100vh - 88rpx - env(safe-area-inset-top));
		flex-direction: column;
		align-items: center;
		justify-content: center;
		background-color: $app-color-theme;
	}

	.logo {
		height: 200rpx;
		width: 200rpx;
		// margin-top: -200rpx;
		margin-left: auto;
		margin-right: auto;
		margin-bottom: 50rpx;
	}

	.text-area {
		display: flex;
		justify-content: center;
	}

	.title {
		font-size: 36rpx;
		color: #fff;
	}
</style>
