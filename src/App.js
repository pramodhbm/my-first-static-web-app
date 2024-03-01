import React, { useState, useEffect } from 'react';

function App(props) {
  const [data, setData] = useState('');

  useEffect(() => {
    (async function () {
      const { text } = await( await fetch(`/api/message`)).json();
      setData(text);
    })();
  });

  const firstName = props.user.firstName;
  const lastName = props.user.lastName;
  return <div>Hello {firstName} {lastName}. {data}</div>;
}

export default App;
