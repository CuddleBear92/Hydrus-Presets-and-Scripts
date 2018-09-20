// ==UserScript==
// @name		Booru Mass Uploader
// @description	Add ability to bulk upload images to your booru
// @namespace 	https://github.com/Seedmanc/Booru-mass-uploader
// @version     1.3.3 EDITED
// @author		Seedmanc
// @include     http://*.booru.org/index.php*
// @include     http://rule34.xxx/index.php*
// @include 	http://gelbooru.com/index.php*
// @include     http://safebooru.org/index.php*
// @include		https://moe.dev.myconan.net/*
// @include		http://behoimi.org/*
// @include		https://chan.sankakucomplex.com/*
// @include		http://atfbooru.ninja/*
// @include		http://danbooru.donmai.us/*
// @include		https://danbooru.donmai.us/*
// @include		http://eikonos.org/*
// @include		https://hydrus.booru.org*

// you can add any boorus of your choice by following the pattern

// @grant 		none
// @run-at		document-end
// @noframes
// ==/UserScript==

if (window.top != window.self) {
	throw 'no iframes';
}

function activateScripts(scripts, i) {
	var node   = scripts[i],
	    parent = node.parentElement,
	    d      = document.createElement('script');

	d.async = node.async;
	d.src = node.src;
	d.onload = function () {
		if (i < scripts.length - 1) {
			activateScripts(scripts, i + 1);
		}
	};
	parent.insertBefore(d, node);
	parent.removeChild(node);
}

if (~document.location.href.indexOf('s=mass_upload')) {
	var script = document.createElement('script');

	document.body.innerHTML = '<img src="https://seedmanc.github.io/Booru-mass-uploader/spinner.gif"/>';
	script.src = 'https://seedmanc.github.io/Booru-mass-uploader/js/index.html.js';
	script.onload = function () {
		var scripts = document.getElementsByTagName('script');

		activateScripts(scripts, 0);
	};
	document.body.appendChild(script);

} else {
	var navbar = document.getElementById('navbar') ||
		document.getElementsByClassName('flat-list2')[0] ||
		document.querySelector('#main-menu > ul') ||
		document.querySelector('nav > menu');
	var li = document.createElement("li");
	var a = document.createElement("a");
	var token = document.querySelector('meta[name="csrf-token"]');

	token = token && token.content;
	if (token) {
		localStorage.setItem('auth_token', token);
	}

	if (document.querySelector('[src*="moe-legacy"]') || document.querySelector('html.action-post') || document.querySelector('[href*="/post/upload"]')) {
		localStorage.setItem('current', 'moebooru');
	} else if (document.querySelector('[href*="/uploads/new"]') || ~document.documentElement.innerHTML.indexOf('Running Danbooru')) {
		localStorage.setItem('current', 'danbooru');
	}

	if (!navbar) {
		throw "can't link the uploader";
	}

	a.style.fontWeight = 'bold';
	a.appendChild(document.createTextNode('Mass Upload'));
	a.href = document.location.protocol + '//' + document.location.hostname + '/index.php?page=post&s=mass_upload';
	li.appendChild(a);
	navbar.appendChild(li);
}