import React from 'react';
import logo from './logo.svg';
import './App.css';

class App extends React.Component {
   constructor(props) {
       super(props)
       this.state = {
           'users': []
       }
   }

componentDidMount() {
   axios.get('http://127.0.0.1:8000/api/users')
       .then(response => {
           const authors = response.data
               this.setState(
               {
                   'users': users
               }
           )
       }).catch(error => console.log(error))
}

   render () {
       return (
           <div>
               Main App
           </div>
       )
   }
}

export default App;