import axios from 'axios';
import { useState } from 'react';
import './Superlogin.css';
function Superlogin() {
  const [name, setname] = useState('');
  const [psw, setpsw] = useState('');
  const [message, setmessage] = useState('');


  const handlelogin = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.post("http://127.0.0.1:8000/superadmin/superlogin/", {
        name,
        psw
      });

      setmessage(response.data.message);
      sessionStorage.setItem('Superuser',name);
    } 
    catch (error) {
      console.log("error");
      setmessage("error");
    }
  };

  return (
    <>
      <h1>SUPER ADMIN LOGIN</h1>
      <form onSubmit={handlelogin}>
        <input
          type="text"
          value={name}
          onChange={(e) => setname(e.target.value)} 
          placeholder="Username"
        />{name}  <br /><br />
        <input
          type="password"
          value={psw}
          onChange={(e) => setpsw(e.target.value)} 
          placeholder="Password"
        />{psw}  <br /><br />
        <button type="submit">Login</button>
      </form>
    </>
  );
}

export default Superlogin;
