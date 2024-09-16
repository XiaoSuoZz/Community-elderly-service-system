<template>
	<view class="content">
		<view class="container">
			<!-- 日期列表 -->
			<scroll-view class="scroll-view_H b-t b-b" scroll-x>
				<block v-for="(item,index) in dateArr" :key="index">
					<div class="flex-box" @click="selectDateEvent(index,item)" :class="{ borderb: index==dateActive}">
						<view class="date-box" :style="{color:index==dateActive?selectedTabColor:'#333'}">
							<text class="fontw">{{item.week}}</text>
							<text>{{item.date}}</text>
						</view>
					</div>
				</block>
			</scroll-view>

			<!-- 时间选项 -->
			<view class="time-box">
				<block v-for="(item,_index) in timeArr" :key="_index">
					<view class="item">
						<view class="item-box" :class="{'disable':item.disable,
						'active':_index==timeActive}"
						 :style="{color:_index==timeActive?selectedItemColor:'#333'}"
						 @click="selectTimeEvent(_index,item)">
							<text>{{item.time}}</text>
							<text class="all">{{item.disable?disableText:undisableText}}</text>
						</view>
					</view>
				</block>
			</view>
		</view>
		<view class="bottom">
			<view class="show-time">
				预约时间：{{orderDateTime}}
			</view>
			<button form-type="submit" type="default" size="mini" class="submit-btn" @click="showPop = true">
				确认预约
			</button>
		</view>
		<u-popup :show="showPop" closeable @close="showPop = false">
			<view class="pop-content">
				<u--form labelPosition="left" labelWidth="100" :model="addInfo" :rules="rules" ref="infoForm">
					<u-form-item label="服务类型" prop="type" borderBottom>
						<u-radio-group v-model="addInfo.type" placement="row">
								<u-radio v-for="item in appointmentTypes" :customStyle="{marginRight: '10px'}" :label="item.name" :name="item.id"></u-radio>
						</u-radio-group>
					</u-form-item>
					<u-form-item label="更多信息" prop="addInfo.detail" borderBottom>
						<u--textarea v-model="addInfo.detail" placeholder="请输入内容" ></u--textarea>
					</u-form-item>
					<u-button type="primary" @click="handleSubmit">提交</u-button>
				</u--form>
			</view>
		</u-popup>
	</view>
</template>

<script>
	import { mapGetters, mapActions } from 'vuex'
	import { getQueryString, formatDate } from '../../../utils/utils.js'
	import {
		initData,
		initTime,
		timeStamp,
		currentTime
	} from '../../../utils/date.js'
	export default {
		name: 'times',
		// model: {
		// 	prop: "showPop",
		// 	event: "change"
		// },
		props: {
			disableText: { //禁用显示的文本
				type: String,
				default: "已约满"
			},
			undisableText: { //未禁用显示的文本
				type: String,
				default: "可预约"
			},
			timeInterval: { // 时间间隔，小时为单位
				type: Number,
				default: 1
			},
			selectedTabColor: { // 日期栏选中的颜色
				type: String,
				default: "#FB4B5C"
			},
			selectedItemColor: { // 时间选中的颜色
				type: String,
				default: "#FB4B5C"
			},
			beginTime: {
				type: String,
				default: "09:00:00"
			},
			endTime: {
				type: String,
				default: "19:00:00"
			}
		},
		data() {
			return {
				orderDateTime: '暂无选择', // 选中时间
				dateArr: [], //日期数据
				timeArr: [], //时间数据
				nowDate: "", // 当前日期
				dateActive: 0, //选中的日期索引
				timeActive: 0, //选中的时间索引
				selectDate: "", //选择的日期
				selectTime: "", //选择的时间
				
				currentDateDisableTimeArr: [], // 当日已被预约的时间
				
				showPop: false,
				rules: {
					'type': {
						type: 'number',
						required: true,
						message: '请选择服务类型',
						trigger: ['blur', 'change']
					},
				},
				appointmentTypes: [
					{ id: 1, name: '家政' },
					{ id: 2, name: '医疗' },
					{ id: 3, name: '药品' },
					{ id: 4, name: '代买' }
				],
				addInfo: {
					type: 1,
					detail: ''					
				}
			}
		},
		computed: {
			...mapGetters([
				'getUserInfo'
			])
		},
		async created(props) {
			this.selectDate = this.nowDate = currentTime().date
			await this.getAppoinmentCurrentDate()
			this.initOnload()
		},
		mounted() {			
			if (!this.getUserInfo) {
				uni.redirectTo({
					url: `../../login/login`
				})
			}
		},
		methods: {
			...mapActions({
				actionAppointmentAdd: 'appointmentAdd',
				actionAppointmentList: 'appointmentList',
				actionAppointmentDateList: 'appointmentDateList'
			}),
			initOnload() {
				this.dateArr = initData() // 日期栏初始化
				this.timeArr = initTime(this.beginTime, this.endTime, this.timeInterval) //时间选项初始化

				let isFullTime = true
				this.timeArr.forEach((item, index) => {
					//判断是当前这一天，选中时间小于当前时间则禁用
					if (this.selectDate == this.nowDate && currentTime().time > item.time) {
						item.disable = true
					}
					
					// 将预约的时间禁用
					this.currentDateDisableTimeArr.forEach(time => {
						if (item.time == time) {
							item.disable = true
						}
					})
							
					// 判断是否当前日期时间都被预约
					if (!item.disable) {
						isFullTime = false
					}
				})

				this.orderDateTime = isFullTime ? "暂无选择" : this.selectDate
				this.timeActive = -1
				for(let i=0,len = this.timeArr.length;i<len;i++) {
					if(!this.timeArr[i].disable) {
						this.orderDateTime = `${this.selectDate} ${this.timeArr[i].time}`
						this.timeActive = i
						this.selectTime = this.timeArr[i].time
						return
					}
				}
			},

			// 日期选择事件
			async selectDateEvent(index, item) {
				this.dateActive = index
				this.selectDate = item.date
				await this.getAppoinmentCurrentDate()
				this.initOnload()
			},

			// 时间选择事件
			selectTimeEvent(index, item) {
				if (item.disable) return
				this.timeActive = index
				this.selectTime = item.time
				this.orderDateTime = `${this.selectDate} ${item.time}`
			},
			// 获取当日已被预约的时间
			async getAppoinmentCurrentDate() {
				this.currentDateDisableTimeArr = []
				const ret = await this.actionAppointmentDateList({ date: this.selectDate })
				if (ret.code == 0) {
					this.currentDateDisableTimeArr = ret.data
				}
			},
			async handleSubmit() {
				console.log(this.selectDate, this.selectTime, this.addInfo)
				
				const para = {
					user_id: this.getUserInfo.id,
					date: this.selectDate,
					time: this.selectTime,
					type: this.addInfo.type,
					detail: this.addInfo.detail
				}
				uni.showLoading({
					mask: true
				})
				const ret = await this.actionAppointmentAdd(para)
				uni.hideLoading()
				if(ret.code == 0) {
					uni.showToast({
						icon: 'none',
						title: '预约成功'
					})
					this.showPop = false
					// this.addInfo.type = 1
					this.addInfo.detail = ''
					await this.getAppoinmentCurrentDate()
					this.initOnload()
				}
			}
		}
	}
</script>
<style lang="scss" scoped>
	@import './pretty-times.scss';

	page {
		height: 100%;
	}

	.content {
		text-align: center;
		height: 100%;
	}
	.pop-content {
		padding: 20px;
	}
	/* 两个按钮 */
	.bottom {
		display: flex;
		flex-direction: row;
		position: fixed;
		bottom: 8px;
		top: auto;
		left: 0px;
		width: 100%;
		background-color: #fff;
	}

	.show-time {
		width: 70%;
		height: 47px;
		color: #505050;
		background-color: rgba(255, 255, 255, 1);
		font-size: 15px;
		line-height: 47px;
		text-align: center;
	}

	.submit-btn {
		width: 25%;
		height: 40px;
		color: white;
		background-color: #CA89FF;
		font-size: 15px;
		line-height: 40px;
		text-align: center;
		margin: auto;
		padding: 0;
	}

	.fontw {
		font-weight: bold;
	}

	.borderb {
		border-bottom: 2px solid #FB4B5C;
	}
</style>
