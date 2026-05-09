"""内置常见主题的识字词汇联想库"""

THEME_VOCABULARY = {
    "超市": {
        "core": [
            ("shōu yín yuán", "收银员"),
            ("huò jià", "货架"),
            ("gòu wù chē", "购物车"),
            ("shōu yín tái", "收银台"),
            ("dǎo gòu", "导购"),
        ],
        "items": [
            ("píng guǒ", "苹果"),
            ("xiāng jiāo", "香蕉"),
            ("niú nǎi", "牛奶"),
            ("miàn bāo", "面包"),
            ("jī dàn", "鸡蛋"),
            ("táng guǒ", "糖果"),
            ("bǐng gān", "饼干"),
            ("kuàng quán shuǐ", "矿泉水"),
        ],
        "environment": [
            ("chū kǒu", "出口"),
            ("rù kǒu", "入口"),
            ("jià gé biāo", "价格标"),
            ("cuò shī", "货架"),
            ("gòu wù lán", "购物篮"),
        ],
    },
    "医院": {
        "core": [
            ("yī shēng", "医生"),
            ("hù shì", "护士"),
            ("bìng chuáng", "病床"),
            ("zhěn shì", "诊室"),
            ("guà hào chù", "挂号处"),
        ],
        "items": [
            ("tīng zhěn qì", "听诊器"),
            ("tǐ wēn jì", "体温计"),
            ("zhù shè qì", "注射器"),
            ("yào pǐn", "药品"),
            ("chuàng kě tiē", "创可贴"),
            ("kòu zhào", "口罩"),
            ("shù yè píng", "输液瓶"),
            ("yào shuǐ", "药水"),
        ],
        "environment": [
            ("jí zhěn", "急诊"),
            ("bìng fáng", "病房"),
            ("shǒu shù shì", "手术室"),
            ("děng hòu qū", "等候区"),
        ],
    },
    "公园": {
        "core": [
            ("yóu lè yuán", "游乐园"),
            ("cǎo píng", "草坪"),
            ("shù mù", "树木"),
            ("huā tán", "花坛"),
            ("hú shuǐ", "湖水"),
        ],
        "items": [
            ("huá tī", "滑梯"),
            ("qiū qiān", "秋千"),
            ("shā tān", "沙滩"),
            ("fēng zhēng", "风筝"),
            ("zì xíng chē", "自行车"),
            ("tī qiú", "踢球"),
            ("yǔ máo qiú", "羽毛球"),
            ("jiǎo huā", "浇花"),
        ],
        "environment": [
            ("cháng yǐ", "长椅"),
            ("lù dēng", "路灯"),
            ("zhǐ shì pái", "指示牌"),
            ("xiǎo lù", "小路"),
        ],
    },
    "动物园": {
        "core": [
            ("dòng wù yuán cháng", "动物园长"),
            ("lóng zi", "笼子"),
            ("wèi dòng wù", "喂动物"),
            ("mén piào chù", "售票处"),
            ("dì tú", "地图"),
        ],
        "items": [
            ("dà xiàng", "大象"),
            ("cháng jǐng lù", "长颈鹿"),
            ("xióng māo", "熊猫"),
            ("shī zi", "狮子"),
            ("hóu zi", "猴子"),
            ("lǎo hǔ", "老虎"),
            ("qǐ é", "企鹅"),
            ("kǒng què", "孔雀"),
        ],
        "environment": [
            ("dòng wù yuán mén", "动物园门"),
            ("cān tīng", "餐厅"),
            ("xiū xī qū", "休息区"),
            ("lù biāo", "路标"),
        ],
    },
    "学校": {
        "core": [
            ("lǎo shī", "老师"),
            ("tóng xué", "同学"),
            ("jiào shì", "教室"),
            ("hēi bǎn", "黑板"),
            ("xiào zhǎng", "校长"),
        ],
        "items": [
            ("shū běn", "书本"),
            ("qiān bǐ", "铅笔"),
            ("xiàng pí", "橡皮"),
            ("chǐ zi", "尺子"),
            ("shū bāo", "书包"),
            ("zuò yè běn", "作业本"),
            ("fěn bǐ", "粉笔"),
            ("jiǎng tái", "讲台"),
        ],
        "environment": [
            ("cāo chǎng", "操场"),
            ("tú shū guǎn", "图书馆"),
            ("shí táng", "食堂"),
            ("jiào xué lóu", "教学楼"),
        ],
    },
    "农场": {
        "core": [
            ("nóng mín", "农民"),
            ("dào tián", "稻田"),
            ("shēng kǒu juàn", "牲口圈"),
            ("guǒ yuán", "果园"),
            ("wēn shì", "温室"),
        ],
        "items": [
            ("gōng jī", "公鸡"),
            ("mǔ jī", "母鸡"),
            ("huáng niú", "黄牛"),
            ("shān yáng", "山羊"),
            ("xiǎo tù", "小兔"),
            ("dà bái cài", "大白菜"),
            ("hú luó bo", "胡萝卜"),
            ("xī hóng shì", "西红柿"),
        ],
        "environment": [
            ("nóng shè", "农舍"),
            ("lí ba", "篱笆"),
            ("tián yě", "田野"),
            ("shuǐ jǐng", "水井"),
        ],
    },
    "餐厅": {
        "core": [
            ("chú shī", "厨师"),
            ("fú wù yuán", "服务员"),
            ("cān zhuō", "餐桌"),
            ("chú fáng", "厨房"),
            ("shōu yín tái", "收银台"),
        ],
        "items": [
            ("wǎn", "碗"),
            ("kuài zi", "筷子"),
            ("sháo zi", "勺子"),
            ("bēi zi", "杯子"),
            ("cān jīn zhǐ", "餐巾纸"),
            ("cài dān", "菜单"),
            ("yǐ zi", "椅子"),
            ("pán zi", "盘子"),
        ],
        "environment": [
            ("cān tīng mén", "餐厅门"),
            ("chuāng hu", "窗户"),
            ("dēng", "灯"),
            ("zhuō bù", "桌布"),
        ],
    },
    "家庭": {
        "core": [
            ("bà ba", "爸爸"),
            ("mā ma", "妈妈"),
            ("yé ye", "爷爷"),
            ("nǎi nai", "奶奶"),
            ("xiǎo hái", "小孩"),
        ],
        "items": [
            ("shā fā", "沙发"),
            ("diàn shì", "电视"),
            ("cān zhuō", "餐桌"),
            ("chuáng", "床"),
            ("shū jià", "书架"),
            ("wán jù", "玩具"),
            ("huā píng", "花瓶"),
            ("zhōng biǎo", "钟表"),
        ],
        "environment": [
            ("kè tīng", "客厅"),
            ("wò shì", "卧室"),
            ("chú fáng", "厨房"),
            ("yáng tái", "阳台"),
        ],
    },
    "海滩": {
        "core": [
            ("hǎi tān", "海滩"),
            ("dà hǎi", "大海"),
            ("bō làng", "波浪"),
            ("shā tān", "沙滩"),
            ("jiù shēng yuán", "救生员"),
        ],
        "items": [
            ("shā zi", "沙子"),
            ("bèi ké", "贝壳"),
            ("hǎi xīng", "海星"),
            ("yáng sǎn", "阳伞"),
            ("tài yáng jìng", "太阳镜"),
            ("yóu yǒng quān", "游泳圈"),
            ("shā tān qiú", "沙滩球"),
            ("chōng làng bǎn", "冲浪板"),
        ],
        "environment": [
            ("yē zi shù", "椰子树"),
            ("tiān kōng", "天空"),
            ("yún", "云"),
            ("hǎi ōu", "海鸥"),
        ],
    },
}


def get_theme_list() -> list[str]:
    """返回所有支持的主题列表"""
    return list(THEME_VOCABULARY.keys())


def get_vocabulary(theme: str) -> dict | None:
    """获取指定主题的词汇"""
    return THEME_VOCABULARY.get(theme)
