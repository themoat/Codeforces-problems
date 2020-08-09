# WebRTC has three main functions, which is to acquire video and audio stream, maintain a connection between
#peers and stream audio/video, communicate arbitrary data.

# WebRTC provides us with 3 JS API's that can be used simply, and they are:
# getUserMedia ---> Access and acquire audio/video streams.
#RTCPeerConnection ----> Establish a connection between peers and stream audio/video.
#RTCDataChannel ----> Communicate arbitrary data.

# So using getUserMedia:

""" var constraints = {video:true};
    functionsuccessCallback(stream){
    // Do things with the stream
    }
    functionerrorCallback(error){
    //uh-oh Error
    }

    navigator.getUserMedia(constraints,successCallback,errorCallback)

"""
# RTCPeer connection does signal processing, noise cancellation,codec handling,p2p communication,security
#and bandwidth management.

#Sample Code:

'''
 pc = new RTCPeerConnection();
 pc.onaddstream = getRemotestream;
 pc.addstream(localstream);
 pc.createdOffer(getOffer)
 
 function getOffer(desc){
    pc.setLocalDescription(desc)
    sendOffer(desc);
    
    }
    
    
    
 function getAnswer(desc){
    pc.setRemoteDescription(desc);
    }
 
 function getRemoteStream(e){
    attachMediaStream(remoteVideo,e.stream)
    }
 '''

#RTC Data Channels is bdirectional communication between client to client, works like websockets,
#except the data transfer has nothing to do with servers in between or any socket connection with servers.
#So it has same api as websockets, unreliable or reliable connection(choose tcp or udp), ultra low latency
# and secure.


#BUT HOW DO PEERS FIND EACH OTHER
#BUT IN WEBRTC THERE ISN'T ANY STANDARD TO FIND PEERS TO EXCHANGE INFO.
#SO HERE WE USE SIGNALLING.

#WEBRTC IS P2P, BUT WE STILL NEED SERVERS TO BUILD CONNECTION.

#So what signalling does, is that we needs servers, to establish connection between client to client or say p2p
#`  1