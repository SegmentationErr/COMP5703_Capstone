<template>
  <div id="line"/>
</template>

<script>
import * as echarts from 'echarts'
import {getLineChartData} from '@/API'

export default {
  name: 'LineChart',
  props: {
    timeInterval: Number
  },
  async created() {
    await this.processData()
  },
  data() {
    return {
      rawData: [],
      beautyData: {},
      option: {}
    }
  },
  methods: {
    splitData(rawData) {
      let pred = [];
      let truth = [];
      for (let i = 0; i < rawData.length; i++) {
        pred.push(rawData[i][0])
        truth.push(rawData[i][1])
      }
      return {
        pred,
        truth
      };
    },
    async processData() {
      const res = await getLineChartData(this.timeInterval);
      this.rawData = res['data']['data']
      this.beautyData = this.splitData(this.rawData);
      this.genOptions()
      const chartDom = document.getElementById('line')
      const myChart = echarts.init(chartDom)
      myChart.clear()
      myChart.setOption(this.option)

    },
    genOptions() {
      this.option = {
        title: {
          text: 'Stacked Line'
        },
        tooltip: {
          trigger: 'axis'
        },
        legend: {
          bottom: 60,
          left: 'center',
          data: ['Prediction', 'Ground truth']
        },
        grid: {
          left: '3%',
          right: '4%',
          bottom: '3%',
          containLabel: true
        },
        xAxis: {
          type: 'category',
          boundaryGap: false,
          data: this.beautyData.categoryData,
        },
        yAxis: {
          type: 'value'
        },
        dataZoom: [
          {
            type: 'inside',
            xAxisIndex: [0, 1],
            start: 98,
            end: 100
          },
          {
            show: true,
            xAxisIndex: [0, 1],
            type: 'slider',
            top: '85%',
            start: 98,
            end: 100
          }
        ],
        series: [
          {
            name: 'Prediction',
            type: 'line',
            // stack: 'Total',
            data: this.beautyData.pred
          },
          {
            name: 'Ground truth',
            type: 'line',
            // stack: 'Total',
            data: this.beautyData.truth
          }
        ]
      }
    }
  },
  watch: {
    timeInterval(){
      this.processData()
    }
  }
}

</script>

<style scoped>
#line {
  width: 1080px;
  height: 400px;
  margin: 0 auto;
}
</style>
