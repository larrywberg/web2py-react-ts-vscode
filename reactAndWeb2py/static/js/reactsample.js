// This is a JS only sample, no JSX or TSX
'use strict';

// This is the main "app" for this view.
class thisApp extends React.Component {
  constructor(props) {
    super(props);
  }
  render() {
      return (
         <div>
            <LikeButton labelOn={this.props.labelOn} labelOff={this.props.labelOff} />
            <br /><br />
            <LikeButtonJSX  labelOn={this.props.labelOn} labelOff={this.props.labelOff} />
         </div>
      );
  }
}

// This is an example class built purely as a function.  No JSX
class LikeButton extends React.Component {
  constructor(props) {
    super(props);
    this.state = { liked: false };
  }

  render() {
    return React.createElement(
      'button',
      { onClick: () => this.setState({ liked: !this.state.liked }) },
        this.state.liked ? this.props.labelOn : this.props.labelOff
    );
  }
}

// This is an example class built with JSX syntax which must be run through babel
class LikeButtonJSX extends React.Component {
  constructor(props) {
    super(props);
    this.state = { liked: false };
  }

  render() {
    return (
      <button onClick={() => this.setState({ liked: !this.state.liked })} >
        { this.state.liked ? this.props.labelOn : this.props.labelOff }
      </button>
    );
  }
}

const domContainer = document.querySelector('#react');
ReactDOM.render(React.createElement(thisApp, window.props), domContainer);
