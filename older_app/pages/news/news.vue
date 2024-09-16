<template>
	<view class="news">
		<u-sticky bgColor="#fff">
			<u-tabs :list="getNewsCateList" @change="onChangeTab"></u-tabs>
		</u-sticky>
		<view class="list-wrpper">
			<view v-if="!loading">
				<view v-if="list.length === 0" class="empty-wrapper">
					<u-empty mode="news" iconSize="180" marginTop="200" text="暂无新闻"></u-empty>
				</view>
				<view class="news-list">
					<view v-for="(item,index) in list" class="news-item" @click="onSelectNews(item)">
						<view class="news-info-wrapper">
							<view class="news-title">{{ item.title }}</view>
							<view class="news-time">{{ item.create_time}}</view>
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
				// 列表
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
				'getNewsCateList'
			])
		},
		async mounted() {
			console.log(111)
			await this.actionNewsCateList()
			console.log(222)
			this.getNewsList()
		},
		methods: {
			...mapActions({
				actionNewsCateList: 'newsCateList',
				actionNewsList: 'newsList'
			}),
			// 切换tab
			onChangeTab(e) {
				const { index } = e
				this.tabIndex = index
				this.getNewsList()
			},
			// 获取列表
			async getNewsList() {
				this.loading = true
				uni.showLoading({
					mask: true
				})
				const ret = await this.actionNewsList(Object.assign({cate_id: this.getNewsCateList[this.tabIndex].id}, this.page))
				uni.hideLoading()
				this.loading = false
				if(ret.code == 0) {
					const { list, total_count } = ret.data
					for (let item of list) {
						item.create_time = formatDate(new Date(item.create_time))
					}
					this.list = list
				}
			},
			// 进入详情页
			onSelectNews(item) {
				const { id, title } = item
				uni.navigateTo({
					url: `./detail/detail?title=${title}&id=${id}`
				})
			}
		}
	}
</script>
<style lang="scss">
.news-list {
	width: 100%;
	padding: 30rpx 20rpx;
	box-sizing: border-box;
	.news-item {
		width: 100%;
		padding: 20rpx;
		border-bottom: solid 1px #F1F1F1;
		display: flex;
		box-sizing: border-box;
		.news-image-wrapper {
			width: 300rpx;
			height: 200rpx;
			flex: 0;
			img {
				width: 300rpx;
				height: 200rpx;
			}
		}
		.news-info-wrapper {
			flex: 1;
			box-sizing: border-box;
			// height: 200rpx;
			display: flex;
			flex-direction: column;
			justify-content: space-between;
			align-items: flex-start;
			padding-left: 20rpx;
			.news-title {
				font-size: 34rpx;
				color: #333;
				font-weight: bold;
				text-indent: 30rpx;
			}
			.news-time {
				color: #999;
				width: 100%;
				text-align: end;
			}
		}
	}
}
</style>
