var Cookies={
	data:null,
	
	init:function(){
		if(this.data!==null){
		return;
		}
	
	this.data={};
	var data=document.cookie.split(';');
	
		for(var i=0, l=data.length; i<l; i++){
		var cookie=data[i].split('=');
		
			if(cookie.length!=2){
			continue;
			}
		
		var index=cookie[0].replace(/(^\s+)|(\s+$)/g,'');
		this.data[index]=cookie[1].replace(/(^\s+)|(\s+$)/g,'') || '';
		this.data[index]=unescape(this.data[index]);
		}
	},
	get:function(id){
	this.init();
	
	return this.data[id];
	},
	set:function(id,value,days,domains){
	this.init();
	
	var expires='';
	
		if(days){
		var date=new Date();
		date.setTime(date.getTime()+(days*24*60*60*1000));
		}
		
		if(domains){
		var domain=window.location.hostname.match(/^(?:[a-z\d\-\.]*\.)?([a-z\d\-]+\.[a-z]+)$/i);
		domain=domain[1];
		}
	
	document.cookie=id+'='+escape(value)+'; '+(days ? 'expires='+date.toGMTString()+'; ' : '')+(domains ? 'domain=.'+domain+'; ' : '')+' path=/';
	
	this.data[id]=value;
	}
};

	function add(id,add){
	var object=document.getElementById(id);
	var value=object.selectedIndex+add;
	
		if(value<0 || value>=object.options.length){
		return false;
		}
	
	object.selectedIndex=value;
	change(id,id);
    calc(); calc1(); calc2(); calc3();
	}
	
	function change(id,name){
	var object=document.getElementById(id);
	
	Cookies.set(name,object.value,8640000,true);
	}

var roundc_select=document.getElementById('roundc');
var separator_select=document.getElementById('separator');
var dsp_select=document.getElementById('dsp');
var angle_select=document.getElementById('angle');
var mapi_select=document.getElementById('mapi');
var acv_select=document.getElementById('acv');
var curr_select=document.getElementById('curr');
var history_select=document.getElementById('history');

var roundc_value=Cookies.get('roundc');
var separator_value=Cookies.get('separator');
var dsp_value=Cookies.get('dsp');
var angle_value=Cookies.get('angle');
var mapi_value=Cookies.get('mapi');
var acv_value=Cookies.get('acv');
var curr_value=Cookies.get('curr');
var history_value=Cookies.get('history');

	if(roundc_value!==undefined){
	roundc_select.value=roundc_value;
	}
	
	if(separator_value!==undefined){
	separator_select.value=separator_value;
	}
	
	if(dsp_value!==undefined){
	dsp_select.value=dsp_value;
	}
	
	if(angle_value!==undefined){
	angle_select.value=angle_value;
	}
	
	if(mapi_value!==undefined){
	mapi_select.value=mapi_value;
	}

	if(acv_value!==undefined){
	acv_select.value=acv_value;
	}

	if(curr_value!==undefined){
	curr_select.value=curr_value;
	}

	if(history_value!==undefined){
	history_select.value=history_value;
	}
	
	roundc_select.onchange=function(){
	Cookies.set('roundc',roundc_select.value,8640000,true);
    calc(); calc1(); calc2(); calc3();
	}
	
	separator_select.onchange=function(){
	Cookies.set('separator',separator_select.value,8640000,true);
    calc(); calc1(); calc2(); calc3();
	}
	
	dsp_select.onchange=function(){
	Cookies.set('dsp',dsp_select.value,8640000,true);
    calc(); calc1(); calc2(); calc3();
	}
	
	angle_select.onchange=function(){
	Cookies.set('angle',angle_select.value,8640000,true);
    calc(); calc1(); calc2(); calc3();
	}
	
	mapi_select.onchange=function(){
	Cookies.set('mapi',mapi_select.value,8640000,true);
    calc(); calc1(); calc2(); calc3();
	}
	
	acv_select.onchange=function(){
	Cookies.set('acv',acv_select.value,8640000,true);
    calc(); calc1(); calc2(); calc3();
	}
	
	curr_select.onchange=function(){
	Cookies.set('curr',curr_select.value,8640000,true);
    calc(); calc1(); calc2(); calc3();
	}
	
	history_select.onchange=function(){
	Cookies.set('history',history_select.value,8640000,true);
	}