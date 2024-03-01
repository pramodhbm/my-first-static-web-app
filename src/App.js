import React from 'react';

function App(props) {
  const firstName = props.user.firstName;
  const lastName = props.user.lastName;
  return <div>Hello {firstName} {lastName}</div>;
}

export default App;
