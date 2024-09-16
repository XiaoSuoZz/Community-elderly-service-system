<template>
	<view class="container">
		<u-gap height="80"></u-gap>
		<u--textarea v-model="advice" placeholder="请给我们留言" ></u--textarea>
		<u-gap height="80"></u-gap>
		<u-button type="primary" @click="onSubmit">发送</u-button>
	</view>
</template>

<script>
	import { mapGetters, mapActions } from 'vuex'
	import { getQueryString, formatDate } from '../../../utils/utils.js'
	export default {
		data() {
			return {
				advice: null
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
		},
		methods: {
			...mapActions({
				actionMessageBoardSend: 'messageBoardSend'
			}),
			async onSubmit() {
				if (!this.advice) {
					uni.showToast({
						icon: 'none',
						title: '请先输入留言'
					})
					return
				}
				uni.showLoading({
					mask: true
				})
				const ret = await this.actionMessageBoardSend({user_id: this.getUserInfo.id, message: this.advice })
				uni.hideLoading()
				this.loading = false
				if(ret.code == 0) {
					uni.showToast({
						icon: 'none',
						title: '留言成功'
					})
					setTimeout(() => {
						uni.navigateBack()
					}, 2000)
				}
			}
		}
	}
</script>

<style lang="scss">
.container {
	padding: 0 30rpx;
}
</style>
