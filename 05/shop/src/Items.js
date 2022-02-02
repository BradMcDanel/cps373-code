import React, { Component } from 'react';

class Items extends Component {
  constructor(props) {
    super(props);
    this.state = { items: []};
  }

  componentDidMount() {
    // this.setState({...});
    // Fill up the items array with data from the document
  }

  render () {
     return (
      <div>
        <p>Items go here!</p>
      </div>
    );
  }
}

export default Items;
