<template>
	<view class="container">
		<view class="list-wrpper">
			<view v-if="!loading">
				<view v-if="list.length === 0" class="empty-wrapper">
					<u-empty mode="history" iconSize="180" marginTop="200" text="暂无记录"></u-empty>
				</view>
				<view class="record-list">
					<view v-for="(item,index) in list" class="record-item">
						<view class="top">
							<view class="time">{{ item.appointment_time }}</view>
							<view class="type">{{ item.type_str}}</view>
						</view>
						<view class="content">
							<view :style="{color: '#007aff'}">{{ item.user_name}}</view>
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
				// 记录列表
				list: [],
				loading: false,
				appointmentTypes: [
					{ id: 1, name: '家政服务' },
					{ id: 2, name: '医疗服务' },
					{ id: 3, name: '药品配送' },
					{ id: 4, name: '代买购物' }
				],
			};
		},
		computed: {
			...mapGetters([
				'getUserInfo'
			])
		},
		mounted() {			
			if (!this.getUserInfo) {
				uni.redirectTo({
					url: `../../login/login`
				})
			}
			this.getAppointmentList()
		},
		methods: {
			...mapActions({
				actionAppointmentList: 'appointmentList'
			}),
			async getAppointmentList() {
				const para = {
					user_id: this.getUserInfo.id,
					page_index: 1,
					page_size: 1000
				}
				this.loading = true
				uni.showLoading({
					mask: true
				})
				const ret = await this.actionAppointmentList(para)
				uni.hideLoading()
				if(ret.code == 0) {
					const { list } = ret.data
					for (let item of list) {
						item.appointment_time = `${item.date} ${item.time}`
						item.create_time = formatDate(new Date(item.create_time))
						item.type_str = this.appointmentTypes.find(type => type.id == item.type).name
					}
					this.list = list
				}
				this.loading = false
			}
		}
	}
</script>

<style lang="scss">
.record-list {
	width: 100%;
	padding: 30rpx 20rpx;
	box-sizing: border-box;
	.record-item {
		width: 100%;
		padding: 20rpx;
		border-bottom: solid 1px #F1F1F1;
		box-sizing: border-box;
		.top {
			width: 100%;
			display: flex;
			justify-content: space-between;
			font-weight: bold;
			.time {
				color: #666;
			}
			.type {
				color: #999;
			}
		}
		.content {
			width: 100%;
			box-sizing: border-box;
			display: flex;
			justify-content: center;
			align-items: center;
			font-size: 60rpx;
			padding: 20rpx;
			font-weight: bold;
		}
	}
}
</style>
