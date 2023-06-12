import React from 'react'
import UrlPabel from './UrlPabel'
import TextPanel from './TextPanel'


const Panels = ({selectedTab,botdata,setbotdata,url,seturl}:any) => {

    console.log("selectedTab: ", selectedTab)
  return (
    <div className='relative rounded-3xl '>
            {
            selectedTab === 'Text' ? (<TextPanel botdata={botdata} setbotdata={setbotdata}/>)
            :
            selectedTab === 'URL' ? (<UrlPabel url={url} seturl={seturl}/>)
            :
            <></>
   
            
            }
        
    </div>
  )
}

export default Panels