

const float EPSILON = 0.001;
const vec3 AMBIENT = vec3(0.6, 0.4, 0.3);
vec3 gDirLight1 = normalize(vec3(-0.1, 0.2, -1));
vec3 gLightPos1 = vec3(-1, 1, -8);

#define SATURATE(x) clamp(x, 0.0, 1.0)
#define NORMOBJ(o,p) normalize(vec3(o(p.xyz + dif.xyy)-o(p.xyz - dif.xyy),o(p.xyz + dif.yxy)-o(p.xyz - dif.yxy),o(p.xyz+dif.yyx)-o(p.xyz-dif.yyx)))
#define PI 3.14159265359
#define HALF_PI (PI / 2.0)
vec4 SPHERE1 = vec4(0, 0, 3, 2.5); //xyz pos, w radius
float genericSphere(vec3 pos, vec4 sphere)
{
	return length(sphere.xyz - pos) - sphere.w;
}

float sphere1(vec3 pos)
{
	return genericSphere(pos, SPHERE1);
}

vec2 getSphereUv(const in vec3 pos, const vec3 center, vec3 norm)
{
	vec3 dir = normalize(pos - center);
	vec2 orz = normalize(dir.xz);
	float sigmaU = 1.0 - (acos(orz.x) / PI);//optimize arccos with fast impl!!!
	float thetaV = acos(dir.y) / PI;
	float u = sigmaU * 0.5 + 0.5;
	float v = thetaV * 0.5 + 0.5;
	return vec2(u, v);
}


vec2 scene(vec3 pos, out vec3 intersectP)
{

    intersectP = pos + vec3(sin(pos.y + iTime),0,0);
    intersectP.y += 0.3*sin(pos.x + iTime);
    intersectP.x -= 0.5*cos(4.0*(pos.y + iTime));
    intersectP.y -= 0.5*cos(2.5+2.3*(pos.x + 3.0*iTime));    
    intersectP.y -= 0.5*sin(0.8+pos.x + 2.0*iTime);
    intersectP.z += 0.1*sin(0.9+pos.x + 1.35*iTime);
    intersectP.x -= 0.2*cos(1.9+0.2*pos.y + 1.4*iTime);    
    intersectP.x += 0.5*sin(1.9+4.2*pos.y + 0.3*iTime);
    intersectP.y += 0.2*cos(2.5+0.7*pos.y + 0.32*iTime);
    intersectP.x += 0.2*sin(4.6+6.5*pos.y + 1.45*iTime);
    intersectP.x -= 0.1*cos(1.9+0.6*pos.y + 0.6*iTime);
        

	float s1 = sphere1(intersectP);
	float d = s1;
	float matId = 1.0;
	return vec2(d, matId);
}

vec2 raymarch(const in vec3 camPos, const in vec3 rayDir, out vec3 posOut, out vec3 pp)
{
	vec2 d = vec2(1000.0, 0.0);
	vec3 pos = camPos;
    vec3 intersectP = vec3(0,0,0);
	for (int i = 0; i < 80; ++i)
	{
		if (d.x < EPSILON)
		{
			continue;
		}
        
		d = scene(pos, intersectP);
        pp = 
		pos += d.x*rayDir;
	}
	posOut = intersectP;
	return d;
}



vec3 norm(vec3 pos, float matId)
{
	vec3 n = vec3(0,0,0);
	vec2 dif = vec2(EPSILON, 0.0);
	n = NORMOBJ(sphere1, pos);	
	
	return n;
}

vec3 material(float matId, vec3 normal, vec3 posOut, out vec3 normOut, out vec3 specTint)
{
	vec3 col = vec3(1,1,1);
	specTint = vec3(1,1,1);
	normOut = normal;
	if (matId == 1.0)
	{
		vec2 uv = getSphereUv(posOut, SPHERE1.xyz, normal);
		col = vec3(0.2,0.5,0.3) ;
		specTint = vec3(0.5, 0.6, 0.2);
		normOut.x += 0.2 * sin(uv.y*uv.x * 150.0) - 0.3 * cos(uv.y * 150.0);
		normOut.y += 0.4 * sin(uv.x*uv.y * 250.0) + 0.3 * cos(uv.x * 150.0);

		normOut = normalize(normOut);
		vec2 newUv = uv.xy + 0.001*normOut.xy;
		
		
		vec2 muls = abs(vec2(1, 1) - 900.0*abs(vec2(mod(newUv.x, 0.003) - 0.0002, mod(newUv.y, 0.003) - 0.0002)));// , );
		normOut.xy -= 0.3 * muls;
		normOut = normalize(normOut);
		
	}
	else if (matId == 2.0)
	{
		col = vec3(1,1,1);
	}
	
	return col;
}

void mainImage( out vec4 fragColor, in vec2 fragCoord )
{
    
	float gAspect = iResolution.x / iResolution.y;    
	vec2 gMouseHomogeneous = 4.0*((iMouse.xy / iResolution.xy) * 2.0 - 1.0);
    
	vec2 uv = fragCoord.xy / iResolution.xy;
	vec3 homogeneousPos = vec3(uv * 2.0 - 1.0, 0.0);
	homogeneousPos.x *= gAspect;
	vec3 camPos = vec3(0, 0, -1);
	vec3 camPivot = vec3(0, 0, 3);
	vec3 seeDir = normalize(camPos - camPivot);
	vec3 screenDir = normalize(homogeneousPos - camPivot);
	float initAngle =  (HALF_PI / 150.0) * (sin(iTime * 2.7));
	float initAngleVet =  (HALF_PI / 150.0) * (cos(iTime * 3.0));
	float angle = HALF_PI + initAngle + (-gMouseHomogeneous.x) * 0.1;//(iTime * 0.9);
	float angleVert = HALF_PI + initAngleVet + (-gMouseHomogeneous.y) * 0.1;//(iTime * 0.9);;
	
	vec2 cosSinAngle = vec2(sin(angle), cos(angle));
	vec2 cosSinAngleVert = vec2(sin(angleVert), cos(angleVert));
	
	seeDir.xz = vec2( dot( seeDir.xz, cosSinAngle.xy ), dot( seeDir.xz, vec2(-cosSinAngle.y, cosSinAngle.x) ) );
	screenDir.xz = vec2( dot( screenDir.xz, cosSinAngle.xy ), dot( screenDir.xz, vec2(-cosSinAngle.y, cosSinAngle.x) ) );
	
	seeDir.yz = vec2( dot( seeDir.yz, cosSinAngleVert.xy ), dot( seeDir.yz, vec2(-cosSinAngleVert.y, cosSinAngleVert.x) ) );
	screenDir.yz = vec2( dot( screenDir.yz, cosSinAngleVert.xy ), dot( screenDir.yz, vec2(-cosSinAngleVert.y, cosSinAngleVert.x) ) );
	
	
	camPos = seeDir * length(camPos - camPivot) + camPivot;
	homogeneousPos = screenDir * length(homogeneousPos - camPivot) + camPivot;
	
	
	
	vec3 rayDir = normalize(homogeneousPos - camPos);
	vec3 finalCol = 2.9*vec3(vec3(1.0 - uv.y) * 0.3) * vec3(0.7,0.7,0.8);
	vec3 posOut; vec3 pp;
	vec2 d = raymarch(camPos, rayDir, posOut, pp);
	if (d.x < EPSILON )
	{
		vec3 lightDir = normalize(gLightPos1 - posOut);
		vec3 n = norm(pp, d.y);
		vec3 normOut = vec3(0,0,0);
		vec3 specTint = vec3(0,0,0);
		vec3 col = material(d.y, n, pp, normOut, specTint);
		vec3 viewVec = normalize(camPos - posOut);
		float diff = max(dot(normOut, lightDir), 0.0);
		vec3 h = normalize(normOut + viewVec);
		vec3 spec = 1.0*pow(max(dot(h, lightDir), 0.0), 64.0)*specTint;
		vec3 fresnel = 0.08*vec3(pow(max(1.0-dot(viewVec, normOut), 0.0),8.0))*specTint;
        
		finalCol =  col*(diff + AMBIENT) + spec + fresnel ;		
	}
	
	fragColor = vec4(pow(finalCol,vec3(2.2)), 1.0);
}