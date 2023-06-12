import React from 'react'

const TextPanel = ({botdata,setbotdata}:any) => {
  return (
        <>
            <textarea value={botdata} onChange={(e:any)=>{setbotdata(e.target?.value)}} id="message" rows={8} className="text-white bg-[#0f0f0f] border-slate-600/30 focus:border-none  hover:ring-slate-600/40 hover:ring-[0.07rem]  px-2  shadow-sm block p-2.5 w-4/5 pb-10 mx-auto text-sm rounded-lg border !outline-none" placeholder="Write your data here..."></textarea>
       </>
  )
}

export default TextPanel