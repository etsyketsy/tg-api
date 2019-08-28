import React, { Component } from 'react';
import { connect } from 'react-redux';


class App extends Component {
    render() {
        return (
            <main className='app'>
                <h1>TG</h1>
            </main>
        );
    };
};
 
const mapStateToProps = state => {
    return {
       state
    };
};

export default connect(mapStateToProps)(App);
