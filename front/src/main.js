import Vue from 'vue'
import './plugins/bootstrap-vue'
import App from './App.vue'
import ApolloClient from 'apollo-boost'
import VueApollo from 'vue-apollo'


const apolloClient = new ApolloClient({
  uri: 'http://0.0.0.0:8000/graphql/'
})

Vue.config.productionTip = false
Vue.use(VueApollo)

const apolloProvider = new VueApollo({
  defaultClient: apolloClient,
})

new Vue({
  apolloProvider,
  render: h => h(App),
}).$mount('#app')
