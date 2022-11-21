<template>
  <div>
    <Header />
    <div class="body">
      <h3>Current trading pair: <span style="color: red">BTC/USD</span></h3>
      <h4>
        Current trading time interval:
        <select v-model="timeInterval">
          <option :value="0.5">30 Minutes</option>
          <option :value="24">Daily</option>
        </select>
      </h4>
      <candle-stick :time-interval="timeInterval"/>
      <line-chart :timeInterval="timeInterval" />
    </div>
  </div>
</template>

<script>
import Header from './components/Header'
import CandleStick from './components/CandleStick'
import LineChart from './components/LineChart'
export default {
  name: 'App',
  components: {
    Header,
    CandleStick,
    LineChart
  },
  data() {
    return {
      timeInterval: 0.5
    }
  }

}
</script>

<style>
body {
  background: rgb(247, 247, 247);
}

#app {
  height: 100vh;
}

.body {
  margin: 80px auto;
  text-align: center;
  max-width: 1180px;
  height: 100%;
  background: white;
}
</style>
