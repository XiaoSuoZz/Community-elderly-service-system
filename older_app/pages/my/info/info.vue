<template>
	<view class="form-wrapper">
		<u--form labelPosition="left" labelWidth="100" :model="info" :rules="rules" ref="infoForm">
			<!-- sub title -->
			<view class="sub-title">账户信息</view>
			<u-form-item label="账户" prop="info.account" borderBottom>
				<u--input v-model="info.account" disabled border="none"></u--input>
			</u-form-item>
			<u-form-item label="密码" prop="info.password" borderBottom>
				<u--input v-model="info.password" border="none"></u--input>
			</u-form-item>
			<view class="sub-title">基本信息</view>
			<u-form-item label="姓名" prop="info.name" borderBottom>
				<u--input v-model="info.name" border="none"></u--input>
			</u-form-item>
			<u-form-item label="联系电话" prop="info.phone" borderBottom>
				<u--input v-model="info.phone" border="none"></u--input>
			</u-form-item>
			<u-form-item label="性别" prop="info.sex" borderBottom @click="showSex = true;">
				<u--input v-model="info.sexStr" disabled disabledColor="#ffffff" placeholder="请选择性别" border="none"></u--input>
				<u-icon slot="right" name="arrow-right"></u-icon>
			</u-form-item>
			<u-form-item label="生日" prop="info.birthDate" borderBottom @click="birthPickerShow = true;">
				<u--input v-model="info.birthDate" disabled disabledColor="#ffffff" placeholder="请选择生日" border="none"></u--input>
				<u-icon slot="right" name="arrow-right"></u-icon>
			</u-form-item>
			<u-form-item label="籍贯" prop="info.birthPlace" borderBottom @click="showBirthPlace= true;">
				<u--input v-model="info.birthPlaceStr" disabled disabledColor="#ffffff" placeholder="请选择籍贯" border="none"></u--input>
				<u-icon slot="right" name="arrow-right"></u-icon>
			</u-form-item>
			<u-form-item label="居住地址" prop="info.areaCode" borderBottom @click="showArea= true;">
				<u--input v-model="info.areaStr" disabled disabledColor="#ffffff" placeholder="请选择地址" border="none"></u--input>
				<u-icon slot="right" name="arrow-right"></u-icon>
			</u-form-item>
			<u-form-item label="详细地址" prop="info.areaDetail" borderBottom>
				<u--textarea v-model="info.areaDetail" autoHeight></u--textarea>
			</u-form-item>
			<!-- sub title -->
			<view class="sub-title">家庭信息</view>
			<u-form-item label="婚姻状况" prop="info.isMarry" borderBottom>
				<u-radio-group v-model="info.isMarry" placement="row">
				    <u-radio :customStyle="{marginRight: '10px'}" label="未婚" :name="0"></u-radio>
				    <u-radio :customStyle="{marginRight: '10px'}" label="已婚" :name="1"></u-radio>
				</u-radio-group>
			</u-form-item>
			<u-form-item label="是否独居" prop="info.isLiveAlone" borderBottom>
				<u-radio-group v-model="info.isLiveAlone" placement="row">
				    <u-radio :customStyle="{marginRight: '10px'}" label="否" :name="0"></u-radio>
				    <u-radio :customStyle="{marginRight: '10px'}" label="是" :name="1"></u-radio>
				</u-radio-group>
			</u-form-item>
			<!-- sub title -->
			<view class="sub-title">紧急联络人</view>
			<u-form-item label="姓名" prop="info.emergencyContactName" borderBottom>
				<u--input v-model="info.emergencyContactName" border="none"></u--input>
			</u-form-item>
			<u-form-item label="联系电话" prop="info.emergencyContactPhone" borderBottom>
				<u--input v-model="info.emergencyContactPhone" border="none"></u--input>
			</u-form-item>
			<u-form-item label="关系" prop="info.emergencyContactRelationship" borderBottom>
				<u--input v-model="info.emergencyContactRelationship" border="none"></u--input>
			</u-form-item>
			<!-- sub title -->
			<view class="sub-title">身体状况</view>
			<u-form-item label="是否残疾" prop="info.isDisability" borderBottom>
				<u-radio-group v-model="info.isDisability" placement="row">
				    <u-radio :customStyle="{marginRight: '10px'}" label="否" :name="0"></u-radio>
				    <u-radio :customStyle="{marginRight: '10px'}" label="是" :name="1"></u-radio>
				</u-radio-group>
			</u-form-item>
			<u-form-item label="疾病史" prop="info.diseasesHistory" borderBottom>
				<view style="width: 100%;">
					<view style="margin: 10rpx 0;" v-for="(item, index) in info.diseasesHistory">
						<u--input v-model="item.content" border="surround">
							<template slot="suffix">
								<u-button @tap="diseasesHistoryDel(index)" icon="trash-fill" type="error" shape="circle" size="mini"></u-button>
							</template>
						</u--input>
					</view>
					<u-button class="add-btn" icon="plus" @click="diseasesHistoryAdd"></u-button>
				</view>
			</u-form-item>
			<u-form-item label="重大疾病史" prop="info.majorDiseasesHistory" borderBottom>
				<view style="width: 100%;">
					<view style="margin: 10rpx 0;" v-for="(item, index) in info.majorDiseasesHistory">
						<u--input v-model="item.content" border="surround">
							<template slot="suffix">
								<u-button @tap="majorDiseasesHistoryDel(index)" icon="trash-fill" type="error" shape="circle" size="mini"></u-button>
							</template>
						</u--input>
					</view>
					<u-button class="add-btn" icon="plus" @click="majorDiseasesHistoryAdd"></u-button>
				</view>
			</u-form-item>
		</u--form>
		<u-gap height="40"></u-gap>
		<u-button type="primary" @click="onSubmit">保存</u-button>
		<!-- 选择器 -->
		<u-action-sheet :show="showSex" :actions="sexOptions" title="请选择性别" cancelText="取消" safeAreaInsetBottom @close="showSex = false" @select="sexSelect"></u-action-sheet>
		<u-datetime-picker :show="birthPickerShow" v-model="info.birthDateTimestamp" :minDate="birthMin" :maxDate="birthMax" mode="date" :formatter="dateFormatter" title="请选择生日" @confirm="onSelectBirth" @cancel="onCloseBirthPicker"></u-datetime-picker>
		<u-picker :show="showBirthPlace" :columns="[areaOptions[0]]" keyName="name" @cancel="showBirthPlace = false" @confirm="birthPlaceSelect" title="请选择籍贯" closeOnClickOverlay></u-picker>
		<u-picker ref="areaPicker" :show="showArea" :columns="areaOptions" keyName="name" @cancel="showArea= false" @change="areaChange" @confirm="areaSelect" title="请选择地址" closeOnClickOverlay></u-picker>
	</view>
</template>

<script>
	import { mapGetters, mapActions } from 'vuex'
	import { formatDate } from '../../../utils/utils.js'
	export default {
		data() {
			return {
				info: {
					id: null, // id
					account: null,
					password: null,
					name: null, // 姓名
					phone: null, // 联系电话
					birthDate: null, // 出生年月日
					birthDateTimestamp: null,
					sex: 0, // 性别 0-男 1-女
					sexStr: "男",
					isMarry: 0, // 是否结婚 0-否 1-是
					isLiveAlone: 0, // 是否独居 0-否 1-是
					isDisability: 0, // 是否残疾 0-否 1-是
					diseasesHistory: [], // 疾病史
					majorDiseasesHistory: [], // 重大疾病史
					emergencyContactName: null, // 紧急联络人姓名
					emergencyContactRelationship: null, // 与紧急联络人关系
					emergencyContactPhone: null, // 紧急联络人电话
					birthPlace: null, // 籍贯 (省id)
					birthPlaceStr: null,
					areaCode: null, // 现住地编号（精确到区县）
					areaStr: null, 
					areaDetail: null, // 现住地详细地址
				},
				// 性别
				showSex: false,
				sexOptions: [
					{ id: 0, name: '男' },
					{ id: 1, name: '女' }
				],
				// 生日选择器
				birthPickerShow: false,
				birthMin: Number(new Date("1930-01-01")),
				birthMax: Number(new Date()),
				// 籍贯
				showBirthPlace: false,
				// 地址
				showArea: false,
				level_1_arr: [],
				level_2_obj: {},
				level_3_obj: {},
				areaOptions: [
					[], [], []
				],
				rules: {
					'name': {
						type: 'string',
						required: true,
						message: '请填写姓名',
						trigger: ['blur', 'change']
					},
					'sex': {
						type: 'string',
						max: 1,
						required: true,
						message: '请选择男或女',
						trigger: ['blur', 'change']
					},
				}
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
			await this.getAreaList()
			this.getUserDetail()
		},
		methods: {
			...mapActions({
				actionAreaList: 'areaList',
				actionUserDetail: 'userDetail',
				actionUserEdit: 'userEdit',
				actionUserLogin: 'login'
			}),
			async getAreaList() {
				const ret = await this.actionAreaList()
				if (ret.code == 0) {
					console.log(ret.data)
					const oriList = ret.data.list
					const level_1_arr = []
					let level_2_obj = {}
					let level_3_obj = {}
					for (let item of oriList) {
						if (item.level == 1) {
							level_1_arr.push({
								code: item.code,
								name: item.name
							})
							level_2_obj[item.code] = []
						} 
					}
					for (let item of oriList) {
						if (item.level == 2) {
							level_2_obj[item.p_code].push({
								code: item.code,
								name: item.name
							})
							level_3_obj[item.code] = []
						}
					}
					for (let item of oriList) {
						if (item.level == 3) {
							if (!level_3_obj[item.p_code]) {
								level_3_obj[item.p_code] = []
								level_2_obj[`${item.p_code.substr(0, 2)}0000`].push({
									code: item.p_code,
									name: item.name
								})
							}
							level_3_obj[item.p_code].push({
								code: item.code,
								name: item.name
							})
						}
					}
					this.level_1_arr = level_1_arr
					this.level_2_obj = level_2_obj
					this.level_3_obj = level_3_obj
				}
			},
			initAreaOptions(area_code) {
				const level_1_code = `${area_code.substr(0, 2)}0000`
				const level_2_code = `${area_code.substr(0, 4)}00`
				const level_3_code = area_code
				let areaOptions = []
				areaOptions[0] = this.level_1_arr
				areaOptions[1] = this.level_2_obj[level_1_code]
				areaOptions[2] = this.level_3_obj[level_2_code]
				console.log('initAreaOptions:', areaOptions)
				this.areaOptions = areaOptions
			},
			async getUserDetail() {
				const para = {
					id: this.getUserInfo.id
				}
				uni.showLoading({
					mask: true
				})
				const ret = await this.actionUserDetail(para)
				uni.hideLoading()
				if(ret.code == 0) {
					const info = ret.data
					info.diseases_history = !info.diseases_history ? [] : JSON.parse(info.diseases_history)
					info.major_diseases_history = !info.major_diseases_history ? [] : JSON.parse(info.major_diseases_history)
					let { id, account, password, name, sex, birth_place_code, 
						birth_place_str, area_code, area_str, area_detail, 
						phone, emergency_contact_name, emergency_contact_phone, 
						emergency_contact_relationship, is_marry, is_live_alone, 
						is_disability, diseases_history, major_diseases_history, birthday, age } = info
					this.initAreaOptions(area_code||'110100')
					let sexStr = '男'
					for (let item of this.sexOptions) {
						if (item.id = sex) {
							sexStr = item.name
							break
						}
					}
					this.info = {
						id, // id
						account, // 账户
						password: password, // 密码
						name, // 姓名
						phone: phone, // 联系电话
						birthDate: birthday, // 出生年月日
						sex, // 性别 0-男 1-女
						sexStr,
						isMarry: is_marry, // 是否结婚 0-否 1-是
						isLiveAlone: is_live_alone, // 是否独居 0-否 1-是
						isDisability: is_disability, // 是否残疾 0-否 1-是
						diseasesHistory: diseases_history.map(item => {return { content: item }}), // 疾病史
						majorDiseasesHistory: major_diseases_history.map(item => {return { content: item }}), // 重大疾病史
						emergencyContactName: emergency_contact_name, // 紧急联络人姓名
						emergencyContactRelationship: emergency_contact_relationship, // 与紧急联络人关系
						emergencyContactPhone: emergency_contact_phone, // 紧急联络人电话
						birthPlace: birth_place_code, // 籍贯 (省id)
						birthPlaceStr: birth_place_str, // 籍贯
						areaCode: area_code, // 现住地编号（精确到区县）
						areaStr: area_str, // 现住地编号（精确到区县）
						areaDetail: area_detail, // 现住地详细地址
					}
				}
			},
			async onSubmit() {
				let { id, account, password, name, phone, 
					birthDate, sex, sexStr, isMarry, isLiveAlone, isDisability, 
					diseasesHistory, majorDiseasesHistory, 
					emergencyContactName, emergencyContactRelationship, emergencyContactPhone, 
					birthPlace, birthPlaceStr, areaCode, areaStr, areaDetail
				} = this.info
				diseasesHistory = JSON.stringify(diseasesHistory.map(item => item.content))
				majorDiseasesHistory = JSON.stringify(majorDiseasesHistory.map(item => item.content))
				const para = {
					id, password, name, phone,
					birthDate, sex, isMarry, isLiveAlone, isDisability, 
					diseasesHistory, majorDiseasesHistory, 
					emergencyContactName, emergencyContactRelationship, emergencyContactPhone, 
					birthPlace, areaCode, areaDetail
				}
				uni.showLoading({
					mask: true
				})
				const ret = await this.actionUserEdit(para)
				uni.hideLoading()
				if(ret.code == 0) {
					this.actionUserLogin({ account, password })
					uni.showToast({
						icon: 'none',
						title: '保存成功'
					})
					setTimeout(() => {
						uni.navigateBack()
					}, 1000)
				}
			},
			// 选择性别
			sexSelect(e) {
				this.info.sex = e.id
				this.info.sexStr = e.name
			}, 
			// 选择籍贯
			birthPlaceSelect(e) {
				console.log(e)
				const { code, name } = e.value[0]
				this.info.birthPlace = code
				this.info.birthPlaceStr = name
				this.showBirthPlace = false
			},
			// 地址改变
			areaChange(e) {
				const { columnIndex, index, indexs, value, picker = this.$refs.areaPicker } = e
				if (columnIndex == 0) {
					picker.setColumnValues(1, this.level_2_obj[this.level_1_arr[index].code])
					picker.setColumnValues(2, this.level_3_obj[this.level_2_obj[this.level_1_arr[index].code][0].code])
				} else if (columnIndex == 1) {
					picker.setColumnValues(2, this.level_3_obj[value[1].code])
				}
			},
			// 选择地址
			areaSelect(e) {
				const len = e.value.length
				this.info.areaCode = e.value[len - 1].code
				let areaStr = ''
				for (let item of e.value) {
					areaStr += `${item.name} `
				}
				this.info.areaStr = areaStr 
				this.showArea = false
			},
			// 选择生日
			onSelectBirth(e) {
				const { value } = e
				this.info.birthDate = formatDate(new Date(value))
				this.onCloseBirthPicker()
			},
			onCloseBirthPicker() {
				this.birthPickerShow = false
			},
			dateFormatter(type, value) {
				if (type === 'year') {
					return `${value}年`
				}
				if (type === 'month') {
					return `${value}月`
				}
				if (type === 'day') {
					return `${value}日`
				}
				return value
			},
			// 疾病史
			diseasesHistoryAdd() {
				this.info.diseasesHistory.push({
					content: ''
				})
			},
			diseasesHistoryDel(index) {
				this.info.diseasesHistory.splice(index, 1)
			},
			// 重大疾病史
			majorDiseasesHistoryAdd() {
				this.info.majorDiseasesHistory.push({
					content: ''
				})
			},
			majorDiseasesHistoryDel(index) {
				this.info.majorDiseasesHistory.splice(index, 1)
			}
		}
	}
</script>

<style lang="scss">
.form-wrapper {
	width: 100%;
	box-sizing: border-box;
	padding: 0 30rpx;
	padding-bottom: 40px;
	.sub-title {
		color: #999999;
		font-size: 28rpx;
		padding-top: 40rpx;
	}
	.add-btn {
		width: 100%;
	}
}
</style>