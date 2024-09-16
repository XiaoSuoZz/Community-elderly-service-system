<template>
	<view class="page">
		<view class="top"></view>
		<view class="user-card card">
			<view class="info-row" @click="onGo('info/info')">
				<view class="label">{{ getUserInfo ? getUserInfo.name : '-' }}</view>
				<view class="arrow"><image src="../../static/icon/arrow-r.png" class="arr-icon"></image></view>
			</view>
		</view>
		<!-- 菜单 -->
		<view class="more-card card">
			<view class="info-row" @click="onGo('record/record')">
				<view class="label">服务记录</view>
				<view class="arrow"><image src="../../static/icon/arrow-r.png" class="arr-icon"></image></view>
			</view>
			<view class="info-row" @click="onGo('favorite/favorite')">
				<view class="label">我的收藏</view>
				<view class="arrow"><image src="../../static/icon/arrow-r.png" class="arr-icon"></image></view>
			</view>
			<view class="info-row" @click="onGo('advice/advice')">
				<view class="label">意见建议</view>
				<view class="arrow"><image src="../../static/icon/arrow-r.png" class="arr-icon"></image></view>
			</view>
		</view>
		
		<view class="more-card card">
			<view class="info-row" @click="onGo('../login/login')">
				<view class="label">退出登录</view>
				<view class="arrow"><image src="../../static/icon/arrow-r.png" class="arr-icon"></image></view>
			</view>
		</view>
	</view>
</template>

<script>
	import { mapGetters, mapActions } from 'vuex'
	export default {
		data() {
			return {};
		},
		computed: {
			...mapGetters([
				'getUserInfo'
			])
		},
		mounted() {			
			if (!this.getUserInfo) {
				uni.redirectTo({
					url: `../login/login`
				})
			}
		},
		methods: {
			onGo(target) {
				uni.navigateTo({
					url: `${target}`
				})
			}
		},
	};
</script>

<style lang="scss" scoped>
	page {
	  background-color:#f8f8f8;
	}
	.top {
		height: 200rpx;
		position: relative;
		background-color: #5199ff;
		border-bottom-left-radius: 22px;
		border-bottom-right-radius: 22px;
	}
	.card {
		margin: 0 30rpx;
		background-color: #fff;
		border-radius: 10rpx;
		width: auto;		
		padding: 20px;
		box-shadow: 2px 2px 20px rgba(0,0,0,.2);
	}
	.user-card {
		position: relative;
		top: -30px;
		font-size: 24px;
		font-weight: bold;
		color: #333;
	}
	.more-card {
		margin-bottom: 30px;
		.info-row {
			border-bottom: 1px solid #F1F1F1;
			padding: 20rpx 0;
			&:last-child {
				border-bottom: none;
			};
		}
	}
	.info-row {
		font-size: 20px;
		width: 100%;
		display: flex;
		justify-content: space-between;
		align-items: center;
		.arr-icon {
			width: 40rpx;
			height: 40rpx;
		}
	}
</style>