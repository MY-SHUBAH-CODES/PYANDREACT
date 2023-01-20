import React, { useState, useEffect } from 'react';
import axios from 'axios';
function App() {
  const[mydata,setMydata]=useState([]);
  useEffect(()=>{
    axios
    .get("http://127.0.0.1:8000/")
    

.then(resp => {
setMydata(resp.data);
    
});



  },[]);

  return (
   <>
   <div style={{'backgroundColor':'green'}}>
   {mydata.map((stu)=>
   {
    const {id,name,age,roll_number}=stu;
    return (
      
    <div className="card" key={id} style={{'color':'white','backgroundColor':'black','height':'100px','width':'300px','marginLeft':'500px'}}>
     <p>{name}</p> 
     <p>{age}</p> 
     <p>{roll_number}</p> 
    </div>
  

    );
   }

   )}
   </div>
   </>
  );
}

export default App;
