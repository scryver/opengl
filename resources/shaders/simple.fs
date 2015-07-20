#version 330 core

in vec2 UV;

// Ouput data
out vec3 color;

uniform sampler2D texSampler;

void main()
{
    // Output color = white
    color = texture2D(texSampler, UV).rgb;
}
