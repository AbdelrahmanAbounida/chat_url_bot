import React from 'react'

export interface TabProp{
    name: string,
}
export const tabs = [
    {
     name:"Text", 
    },
    {
     name:"URL", 
    }
]

const Tabs = ({selectedTab, setselectedTab}:any) => {
  return (
    <div className=''>
        <div
            role='tablist'
            aria-label="tabs"
            className='border-[0.05rem] border-teal-500/70 relative  mx-auto grid grid-cols-2 w-1/2 items-center rounded-lg md:rounded-2xl my-3 shadow-2xl shadow-900/20 transition  overflow-hidden'
            >
                {
                    tabs.map((tab)=>(
                        <button 
                key={tab.name}
                onClick={(e)=>{e.preventDefault();setselectedTab(tab.name)}}
                role='tab'
                aria-selected="true"
                aria-controls='panel-1'
                id='tab-1'
                tabIndex={0}
                className={`relative block h-10 px-6 tab rounded-lg md:rounded-2xl text-white text-xl font-semibold ${tab.name === selectedTab && 'bg-teal-500' } ${tab.name !== selectedTab && 'hover:bg-[#1a2424]'}`}
                >
                    {tab.name}
                </button>
                    ))
                }

        </div>
    </div>
  )
}

export default Tabs