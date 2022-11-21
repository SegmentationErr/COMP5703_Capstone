import axios from 'axios'

export function getTradeData(timeInterval) {
    return axios.get('http://localhost:8999/candleData', {
        params: {timeInterval}
    })
}


export function getLineChartData(timeInterval) {
    return axios.get('http://localhost:8999/lineData', {
        params: {timeInterval}
    })
}
