import Vue from 'vue';
import VueRouter from 'vue-router';
// import Home from '../views/Home.vue';
import Test from '../components/Test.vue';
import HighchartsVue from 'highcharts-vue'

Vue.use(VueRouter);
Vue.use(HighchartsVue);

const routes = [
    {
        path: '/test',
        name: 'Test',
        component: Test,
    }
];

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes,
});

export default router;
