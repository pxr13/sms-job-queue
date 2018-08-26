import React from 'react';
import { Provider } from 'react-redux';
import { render } from 'react-dom';
import store from './redux';
import App from 'components/App';

window.store = store;

render(
  <Provider store={store}>
    <App />
  </Provider>,
  document.getElementById('root')
);
