import { createStore } from 'redux';

import masterReducer from './reducers/index.js';


const store = createStore(masterReducer);

export default store;