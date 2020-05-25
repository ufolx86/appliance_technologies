<template>
    <div>
        <p>{{ msg }}</p>
        <!-- <highcharts :options="chartOptions"></highcharts> -->
    </div>
</template>

<script>
import axios from 'axios';
import {stockChart} from 'highcharts-vue'
    export default {
        name: 'Test',
        components: {
            highCharts: stockChart
        },
        data() {
            return {
                msg: 'Hello!',
                // chartOptions: {
                //     chart: {
                //         height: 400,
                //         type: 'line'
                //     },
                //     title: {
                //         text: 'BITCOIN PRICES SINCE JANUARY 2020'
                //     },
                //     series: [{
                //         name:'Price',
                //         data: [3, 5, 6, 9],
                //         color: 'red'
                //         // data: [
                //         //     ['us-ny', 0],
                //         //     ['us-mi', 5],
                //         //     ['us-tx', 3],
                //         //     ['us-ak', 5]
                //         // ]
                //     }]
                // },
            };
        },
        methods: {
            getDataFromBack() {
                const path = 'http://localhost:5000/test';
                axios.get(path)
                    .then((res) => {
                        this.msg = res.data;
                    })
                    .catch((error) => {
                        console.error(error);
                    });
            }
        },
        created() {
            this.getDataFromBack();
            //msgDataType = typeof this.msg
        },
        // mounted: function () {
        //     setTimeout(function(){ 
        //         //this.message = 'Data Fetched';
        //         this.chartOptions.series[0].data = [3, 5, 6, 9];
        //     }.bind(this), 3000);
        // }
    };
</script>