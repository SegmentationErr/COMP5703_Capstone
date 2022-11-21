<template>
 <div>
   <v-chart
       id="main"
       :option="option"
       :update-options="{ notMerge: true }"
   />
 </div>
</template>

<script>
import VChart from 'vue-echarts'
import { use } from 'echarts/core'
import { SVGRenderer } from 'echarts/renderers'
import {
  TitleComponent,
  AxisPointerComponent,
  TooltipComponent,
  LegendComponent,
  ToolboxComponent,
  BrushComponent,
  VisualMapComponent,
  GridComponent,
  DataZoomComponent
} from 'echarts/components';

use([
  TitleComponent,
  SVGRenderer,
  AxisPointerComponent,
  TooltipComponent,
  LegendComponent,
  ToolboxComponent,
  BrushComponent,
  VisualMapComponent,
  GridComponent,
  DataZoomComponent
])

import {getTradeData} from '@/API'

// const upColor = '#00da3c'
// const downColor = '#ec0000'

export default {
  name: 'CandleStick',
  components: {
    VChart,
  },
  async created() {
    const res = await this.getData()
    this.rawData = res['data']['data']
    this.processData();
    this.genOptions()
  },
  data() {
    return {
      rawData: [],
      beautyData: {},
      option: {
        title: { text: "Column Chart" },
        tooltip: {},
        xAxis: {
          data: ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"],
        },
        yAxis: {},
        series: [
          {
            name: "销量",
            type: "bar",
            data: [5, 20, 36, 10, 10, 20],
          },
        ],
      }
    }
  },
  methods: {
    calculateMA(dayCount, data) {
    const result = [];
    for (let i = 0, len = data.values.length; i < len; i++) {
      if (i < dayCount) {
        result.push('-');
        continue;
      }
      let sum = 0
      for (let j = 0; j < dayCount; j++) {
        sum += data.values[i - j][1];
      }
      result.push(+(sum / dayCount).toFixed(3));
    }
    return result;
    },
    splitData(rawData) {
      let categoryData = [];
      let values = [];
      let volumes = [];
      for (let i = 0; i < rawData.length; i++) {
        categoryData.push(rawData[i].splice(0, 1)[0]);
        values.push(rawData[i]);
        volumes.push([i, rawData[i][4], rawData[i][0] > rawData[i][1] ? 1 : -1]);
      }
      return {
        categoryData: categoryData,
        values: values,
        volumes: volumes
      };
    },
    getData() {
       return getTradeData(1);
    },
    processData() {
      this.beautyData = this.splitData(this.rawData);
      // this.myChart.setOption(option, {notMerge: true})
      // this.myChart.dispatchAction({
      //   type: 'brush',
      //   areas: [
      //     {
      //       brushType: 'lineX',
      //       coordRange: ['2016-06-02', '2016-06-20'],
      //       xAxisIndex: 0
      //     }
      //   ]
      // })
      // if (option && typeof option === 'object') {
      //   this.myChart.setOption(option);
      // }
      // window.addEventListener('resize', this.myChart.resize);
    },
    genOptions() {
      // this.option = {
      //   animation: false,
      //       legend: {
      //     bottom: 10,
      //         left: 'center',
      //         data: ['Dow-Jones index', 'MA5', 'MA10', 'MA20', 'MA30']
      //   },
      //   tooltip: {
      //     trigger: 'axis',
      //         axisPointer: {
      //       type: 'cross'
      //     },
      //     borderWidth: 1,
      //         borderColor: '#ccc',
      //         padding: 10,
      //         textStyle: {
      //       color: '#000'
      //     },
      //     position: function (pos, params, el, elRect, size) {
      //       const obj = {
      //         top: 10
      //       };
      //       obj[['left', 'right'][+(pos[0] < size.viewSize[0] / 2)]] = 30;
      //       return obj;
      //     }
      //   },
      //   axisPointer: {
      //     link: [
      //       {
      //         xAxisIndex: 'all'
      //       }
      //     ],
      //         label: {
      //       backgroundColor: '#777'
      //     }
      //   },
      //   toolbox: {
      //     feature: {
      //       dataZoom: {
      //         yAxisIndex: false
      //       },
      //       brush: {
      //         type: ['lineX', 'clear']
      //       }
      //     }
      //   },
      //   brush: {
      //     xAxisIndex: 'all',
      //         brushLink: 'all',
      //         outOfBrush: {
      //       colorAlpha: 0.1
      //     }
      //   },
      //   visualMap: {
      //     show: false,
      //         seriesIndex: 5,
      //         dimension: 2,
      //         pieces: [
      //       {
      //         value: 1,
      //         color: downColor
      //       },
      //       {
      //         value: -1,
      //         color: upColor
      //       }
      //     ]
      //   },
      //   grid: [
      //     {
      //       left: '10%',
      //       right: '8%',
      //       height: '50%'
      //     },
      //     {
      //       left: '10%',
      //       right: '8%',
      //       top: '63%',
      //       height: '16%'
      //     }
      //   ],
      //       xAxis: [
      //     {
      //       type: 'category',
      //       data: this.beautyData.categoryData,
      //       boundaryGap: false,
      //       axisLine: { onZero: false },
      //       splitLine: { show: false },
      //       min: 'dataMin',
      //       max: 'dataMax',
      //       axisPointer: {
      //         z: 100
      //       }
      //     },
      //     {
      //       type: 'category',
      //       gridIndex: 1,
      //       data: this.beautyData.categoryData,
      //       boundaryGap: false,
      //       axisLine: { onZero: false },
      //       axisTick: { show: false },
      //       splitLine: { show: false },
      //       axisLabel: { show: false },
      //       min: 'dataMin',
      //       max: 'dataMax'
      //     }
      //   ],
      //       yAxis: [
      //     {
      //       scale: true,
      //       splitArea: {
      //         show: true
      //       }
      //     },
      //     {
      //       scale: true,
      //       gridIndex: 1,
      //       splitNumber: 2,
      //       axisLabel: { show: false },
      //       axisLine: { show: false },
      //       axisTick: { show: false },
      //       splitLine: { show: false }
      //     }
      //   ],
      //       dataZoom: [
      //     {
      //       type: 'inside',
      //       xAxisIndex: [0, 1],
      //       start: 98,
      //       end: 100
      //     },
      //     {
      //       show: true,
      //       xAxisIndex: [0, 1],
      //       type: 'slider',
      //       top: '85%',
      //       start: 98,
      //       end: 100
      //     }
      //   ],
      //       series: [
      /*    {*/
      /*      name: 'Dow-Jones index',*/
      /*      type: 'candlestick',*/
      /*      data: this.beautyData.values,*/
      /*      itemStyle: {*/
      /*        color: upColor,*/
      /*        color0: downColor,*/
      /*        borderColor: undefined,*/
      /*        borderColor0: undefined*/
      /*      },*/
      /*      tooltip: {*/
      /*        formatter: function (param) {*/
      /*          param = param[0];*/
      /*          return [*/
      /*            'Date: ' + param.name + '<hr size=1 style="margin: 3px 0">',*/
      /*            'Open: ' + param.data[0] + '<br/>',*/
      /*            'Close: ' + param.data[1] + '<br/>',*/
      /*            'Lowest: ' + param.data[2] + '<br/>',*/
      /*            'Highest: ' + param.data[3] + '<br/>'*/
      /*          ].join('');*/
      /*        }*/
      /*      }*/
      /*    },*/
      /*    {*/
      //       name: 'MA5',
      //       type: 'line',
      //       data: this.calculateMA(5, this.beautyData),
      //       smooth: true,
      //       lineStyle: {
      //         opacity: 0.5
      //       }
      //     },
      //     {
      //       name: 'MA10',
      //       type: 'line',
      //       data: this.calculateMA(10, this.beautyData),
      //       smooth: true,
      //       lineStyle: {
      //         opacity: 0.5
      //       }
      //     },
      //     {
      //       name: 'MA20',
      //       type: 'line',
      //       data: this.calculateMA(20, this.beautyData),
      //       smooth: true,
      //       lineStyle: {
      //         opacity: 0.5
      //       }
      //     },
      //     {
      //       name: 'MA30',
      //       type: 'line',
      //       data: this.calculateMA(30, this.beautyData),
      //       smooth: true,
      //       lineStyle: {
      //         opacity: 0.5
      //       }
      //     },
      //     {
      //       name: 'Volume',
      //       type: 'bar',
      //       xAxisIndex: 1,
      //       yAxisIndex: 1,
      //       data: this.beautyData.volumes
      //     }
      //   ]
      // }
    }
  }
}

</script>

<style scoped>
#main {
  width: 1080px;
  height: 500px;
  margin: 0 auto;
}
.container {
  margin: auto;
}
</style>
