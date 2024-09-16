<template>
	<view class="video">
		<u-sticky bgColor="#fff">
			<u-tabs :list="getVideoCateList" @change="onChangeTab"></u-tabs>
		</u-sticky>
		<view class="list-wrpper">
			<view v-if="!loading">
				<view v-if="list.length === 0" class="empty-wrapper">
					<u-empty mode="news" iconSize="180" marginTop="200" text="暂无视频"></u-empty>
				</view>
				<view class="video-list">
					<view v-for="(item,index) in list" class="video-item" @click="onSelectVideo(item)">
						<view class="video-image-wrapper">
							<img :src="item.img_url"></img>
						</view>
						<view class="video-info-wrapper">
							<view class="video-title">{{ item.title }}</view>
							<view class="video-time">{{ item.create_time}}</view>
						</view>
					</view>
				</view>
			</view>
		</view>
	</view>
</template>

<script>
	import { mapGetters, mapActions } from 'vuex'
	import { formatDate } from '../../utils/utils.js'
	export default {
		data() {
			return {
        tabIndex: 0,
				// 视频列表
				list: [],
				loading: false,
				// 分页
				page: {
					page_index: 1,
					page_size: 10,
					total_count: 0
				}
			};
		},
		computed: {
			...mapGetters([
				'getVideoCateList'
			])
		},
		async mounted() {
			await this.actionVideoCateList()
			this.getVideoList()
		},
		methods: {
			...mapActions({
				actionVideoCateList: 'videoCateList',
				actionVideoList: 'videoList'
			}),
			// 切换tab
			onChangeTab(e) {
				const { index } = e
				this.tabIndex = index
				this.getVideoList()
			},
			// 获取视频列表
			async getVideoList() {
				this.loading = true
				uni.showLoading({
					mask: true
				})
				const ret = await this.actionVideoList(Object.assign({cate_id: this.getVideoCateList[this.tabIndex].id}, this.page))
				uni.hideLoading()
				this.loading = false
				if(ret.code == 0) {
					const { list, total_count } = ret.data
					for (let item of list) {
						item.img_url = `api/${item.img_url}`
						item.create_time = formatDate(new Date(item.create_time))
					}
					this.list = list
				}
			},
			// 进入详情页
			onSelectVideo(item) {
				const { id, title } = item
				uni.navigateTo({
					url: `./detail/detail?title=${title}&id=${id}`
				})
			}
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
</style>
